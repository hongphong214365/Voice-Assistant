import os
import tempfile
import sounddevice as sd
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
from scipy.io.wavfile import write
import speech_recognition as sr
from sound import play


def listen():
    fs = FS
    seconds = RECORD_SECONDS
    if DEBUG:
        print("Tôi đang nghe đây")
    os.makedirs(AUDIO_DIR, exist_ok=True)
    play(START_SOUND)
    try:
        recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype="int16")
        sd.wait()
    except Exception as e:
        print("Lỗi khi thu âm:", e)
        return None

    tmp = None
    try:
        with tempfile.NamedTemporaryFile(
            suffix=".wav", dir=AUDIO_DIR, delete=False
        ) as f:
            tmp = f.name
            write(tmp, fs, recording)
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
