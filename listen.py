import sounddevice as sd
from config import LANG
from scipy.io.wavfile import write
import speech_recognition as sr
def listen():
    fs = 44100
    seconds = 5

    print("Tôi đang nghe đây")
    recording = sd.rec(
    int(seconds * fs),
        samplerate=fs,
        channels=1,
        dtype='int16'
    )
    sd.wait()
    write("audio/record.wav", fs, recording)
    print("đang nhận diện")
    r = sr.Recognizer()
    with sr.AudioFile("audio/record.wav") as source:
        audio = r.record(source)
    try:
        text = r.recognize_google(
            audio,
            language=LANG,
        )
    except sr.UnknownValueError:
        print("Tôi chưa nghe rõ")
        return None
    except sr.RequestError:
        print("Có lỗi kết nối mạng đã xảy ra")
        return None

    return text