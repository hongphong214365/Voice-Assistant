from listen import listen
from brain import think
from speak import speech
while True:
    text = listen()

    if not text:
        continue
    if "tạm biệt" in text.lower():
        speech("Tạm biệt bạn")
        break

    reply = think(text)


    speech(reply)
