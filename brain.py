from datetime import datetime
from config import LANG
def think(text):
    text = text.lower()

    # Xin chào.
    if (
        "xin chào" in text
        or "hello" in text
    ):
        if LANG.startswith("vi"):
            return "Chào bạn"
        return "hello"
    # Hỏi tên.
    if "bạn tên gì vậy" in text:
        return "Tôi là trợ lí ảo của bạn"
    # Hỏi giờ.
    if (
        "mấy giờ rồi" in text
        or "what time is it" in text
    ):
        now = datetime.now()
        if LANG.startswith("vi"):
            return f"Bây giờ là {now.hour} giờ {now.minute} phút"
        return f"It is {now.hour}:{now.minute}"
else:
        return "Tôi không hiểu, bạn thử nói lại nhé"