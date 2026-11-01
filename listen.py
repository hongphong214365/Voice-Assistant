import os
import sys
import tempfile
import wave
from config import (
    LANG,
    AUDIO_DIR,
    FS,
    RECORD_SECONDS,
    DEBUG,
    START_SOUND,
    SUCCESS_SOUND,
    ERROR_SOUND,
)
import speech_recognition as sr
from sound import play


def _load_sounddevice():
    if sys.platform == "win32" and getattr(sys, "frozen", False):
        # PortAudio's stderr redirection corrupts file handles in frozen
        # Windows apps; make sounddevice skip that optional redirection.
        original_dup = os.dup

        def safe_dup(fd):
            if fd == 2:
                raise OSError("stderr redirection disabled in frozen app")
            return original_dup(fd)

        os.dup = safe_dup
        try:
            import sounddevice as sd
        finally:
            os.dup = original_dup
        return sd

    import sounddevice as sd

    return sd


sd = _load_sounddevice()


def listen():
    seconds = RECORD_SECONDS
    if DEBUG:
        print("Tôi đang nghe đây")
    os.makedirs(AUDIO_DIR, exist_ok=True)
    play(START_SOUND)
    try:
        device = sd.query_devices(kind="input")
        fs = FS
        try:
            sd.check_input_settings(samplerate=fs, channels=1, dtype="int16")
        except sd.PortAudioError:
            # Windows microphones commonly run at 48 kHz; use the device's
            # native rate when the configured 44.1 kHz rate is unsupported.
            fs = int(device["default_samplerate"])
            sd.check_input_settings(samplerate=fs, channels=1, dtype="int16")
        with sd.RawInputStream(samplerate=fs, channels=1, dtype="int16") as stream:
            recording, _ = stream.read(int(seconds * fs))
    except Exception as e:
        message = str(e).encode("ascii", errors="backslashreplace").decode()
        print("Audio recording failed:", message)
        return None

    tmp = None
    try:
        with tempfile.NamedTemporaryFile(
            suffix=".wav", dir=AUDIO_DIR, delete=False
        ) as f:
            tmp = f.name
            with wave.open(tmp, "wb") as wav_file:
                wav_file.setnchannels(1)
                wav_file.setsampwidth(2)
                wav_file.setframerate(fs)
                wav_file.writeframes(recording)
        if DEBUG:
            print("đang nhận diện")
        r = sr.Recognizer()
        with sr.AudioFile(tmp) as source:
            audio = r.record(source)
        try:
            text = r.recognize_google(audio, language=LANG)
            play(SUCCESS_SOUND)
        except sr.UnknownValueError:
            play(ERROR_SOUND)
            print("Tôi chưa nghe rõ")
            return None
        except sr.RequestError:
            play(ERROR_SOUND)
            print("Có lỗi kết nối mạng đã xảy ra")
            return None
        return text
    finally:
        try:
            if tmp and os.path.exists(tmp):
                os.remove(tmp)
        except Exception:
            pass
