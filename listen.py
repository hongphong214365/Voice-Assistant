import os
import tempfile
import sounddevice as sd
from config import LANG, AUDIO_DIR, FS, RECORD_SECONDS
from scipy.io.wavfile import write
import speech_recognition as sr

def listen():
    fs = FS
    seconds = RECORD_SECONDS

    print("Tôi đang nghe đây")
    os.makedirs(AUDIO_DIR, exist_ok=True)

    try:
        recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype='int16')
        sd.wait()
    except Exception as e:
        print("Lỗi khi thu âm:", e)
        return None

    tmp = None
    try:
        with tempfile.NamedTemporaryFile(suffix=".wav", dir=AUDIO_DIR, delete=False) as f:
            tmp = f.name
            write(tmp, fs, recording)
        print("đang nhận diện")
        r = sr.Recognizer()
        with sr.AudioFile(tmp) as source:
            audio = r.record(source)
        try:
            text = r.recognize_google(audio, language=LANG)
        except sr.UnknownValueError:
            print("Tôi chưa nghe rõ")
            return None
        except sr.RequestError:
            print("Có lỗi kết nối mạng đã xảy ra")
            return None
        return text
    finally:
        try:
            if tmp and os.path.exists(tmp):
                os.remove(tmp)
        except Exception:
            pass
