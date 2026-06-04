from listen import listen
from brain import think
from speak import speech
while True:
    text = listen()

    if not text:
        contenue
    if "tạm biệt" in text.lower():
        speech("Tạm biệt bạn")
        break

    reply = think(text)


    speech(reply)
# anh thấy sai thụt lề thì khả năng là do em gửi thôi code gốc chạy ngon nha.