from listen import listen
from brain import think
from speak import speech
from config import LANG
while True:
    text = listen()

    if not text:
        continue
    print("bạn",  text)
    if any(word in text.lower() for word in (
        "tạm biệt bạn",
        "bye",
        "kết thúc",
        "tạm biệt",
        "thoát",
        "good bye",
        "goodbye"
    )):
        if LANG.startswith("vi"):
            speech("Tạm biệt bạn, cần giúp gì thì nói mình nhé")
        else:
            speech("good bye")
        break

    reply = think(text)


    speech(reply)
