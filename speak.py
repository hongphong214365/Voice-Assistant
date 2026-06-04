from gtts import gTTS
import pygame
def speech(text):
    tts = gTTS(
        text=text,
        lang="vi",
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
