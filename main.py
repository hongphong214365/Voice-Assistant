from listen import listen
from brain import think
from speak import speech
while True:
    text = listen()

    if not text:
        continue
    print("bạn",  text)
    if any(word in text.lower() for word in (
        "tạm biệt bạn",
        "bye bạn",
        "kết thúc",
        "tạm biệt",
        "thoát",
    )):
        speech("Tạm biệt bạn, cần giúp gì thì nói mình nhé")
        break

    reply = think(text)


    speech(reply)
