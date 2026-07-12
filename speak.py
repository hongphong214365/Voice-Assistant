from gtts import gTTS
import pygame
import tempfile
import os
from config import LANG, AUDIO_DIR


def speech(text):
    # generate TTS to a temporary file inside audio dir
    os.makedirs(AUDIO_DIR, exist_ok=True)
    tmp = None
    try:
        with tempfile.NamedTemporaryFile(
            suffix=".mp3", dir=AUDIO_DIR, delete=False
        ) as f:
            tmp = f.name
        tts = gTTS(text=text, lang=LANG.split("-")[0])
        tts.save(tmp)

        # init mixer with exception handling
        try:
            pygame.mixer.init()
            pygame.mixer.music.load(tmp)
            pygame.mixer.music.play()
            # wait with small sleep to avoid busy-wait
            while pygame.mixer.music.get_busy():
                pygame.time.wait(100)
            pygame.mixer.music.unload()
        except Exception as e:
            print("Lỗi phát âm thanh:", e)
    except Exception as e:
        print("Lỗi TTS:", e)
    finally:
        try:
            if tmp and os.path.exists(tmp):
                os.remove(tmp)
        except Exception:
            pass
