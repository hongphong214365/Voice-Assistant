import time
import sounddevice as sd
import speech_recognition as sr
import numpy as np
from config import LANG, FS, DEBUG, START_SOUND, SUCCESS_SOUND, ERROR_SOUND

from sound import play


CHANNELS = 1
DTYPE = "int16"

SILENCE_DURATION = 0.8
SILENCE_THRESHOLD = 500
BLOCK_DURATION = 0.1
BLOCK_SIZE = int(FS * SILENCE_DURATION)


def listen():
    if DEBUG:
        print("Tôi đang nghe đây")

    play(START_SOUND)

    frames = []
    speaking = False
    silence_start = None

    try:
        with sd.InputStream(
            samplerate=FS,
            channels=CHANNELS,
            dtype=DTYPE,
            blocksize=BLOCK_SIZE,
        ) as stream:
            while True:
                data, overflowed = stream.read(BLOCK_SIZE)

                if overflowed and DEBUG:
                    print("Cảnh báo: audio buffer bị tràn")

                frames.append(data.copy())

                volume = np.abs(data.astype(np.int32)).mean()

                if volume > SILENCE_THRESHOLD:
                    speaking = True
                    silence_start = None

                    if DEBUG:
                        print("Đang nói...", end="\r")

                elif speaking:
                    if silence_start is None:
                        silence_start = time.monotonic()

                    elif time.monotonic() - silence_start >= SILENCE_DURATION:
                        break

    except Exception as e:
        print("Lỗi khi thu âm:", e)
        play(ERROR_SOUND)
        return None

    if not frames:
        play(ERROR_SOUND)
        return None

    recording = np.concatenate(frames, axis=0)

    raw_data = recording.tobytes()

    audio = sr.AudioData(
        raw_data,
        FS,
        recording.dtype.itemsize,
    )

    if DEBUG:
        print("\nđang nhận diện")

    r = sr.Recognizer()

    try:
        text = r.recognize_google(audio, language=LANG)
        play(SUCCESS_SOUND)
        return text

    except sr.UnknownValueError:
        play(ERROR_SOUND)
        print("Tôi chưa nghe rõ")
        return None

    except sr.RequestError:
        play(ERROR_SOUND)
        print("Có lỗi kết nối mạng đã xảy ra")
        return None
