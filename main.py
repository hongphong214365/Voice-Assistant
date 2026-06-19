import os
from listen import listen
from brain import think
from speak import speech
from config import LANG, AUDIO_DIR

# ensure audio dir exists
os.makedirs(AUDIO_DIR, exist_ok=True)

def main():
    try:
        while True:
            text = listen()
            if not text:
                continue
            print("bạn", text)
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
    except KeyboardInterrupt:
        print("\nExiting...")
    except Exception as e:
        print("Đã xảy ra lỗi:", e)

if __name__ == "__main__":
    main()
