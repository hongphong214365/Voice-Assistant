from gtts import gTTS
import pygame
from config import LANG
def speech(text):
    tts = gTTS(
        text=text,
        lang=LANG.split("-")[0],
    )
# Lưu file
    tts.save("audio/Voice.mp3")
# Phát file
    pygame.mixer.init()
    pygame.mixer.music.load(
"audio/Voice.mp3"
    )
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pass
    pygame.mixer.music.unload()
