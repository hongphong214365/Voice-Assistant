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
    if (
        "bạn tên gì vậy" in text
        or "bạn tên gì" in text
        or "what is your name" in text
        or "what's your name" in text
    ):
        if LANG.startswith("vi"):
            return "Tôi là trợ lí ảo của bạn"
        return "I am your virtual assistant"

    # Hỏi giờ.
    if (
        "mấy giờ rồi" in text
        or "what time is it" in text
    ):
        now = datetime.now()
        if LANG.startswith("vi"):
            return f"Bây giờ là {now.hour} giờ {now.minute} phút"
        return f"It is {now.hour}:{now.minute}"

    # Hỏi ngày tháng năm.
    if (
        "hôm nay là ngày mấy" in text
        or "ngày mấy" in text
        or "ngày bao nhiêu" in text
        or "what is today's date" in text
        or "what's today's date" in text
        or "what is the date today" in text
        or "what's the date" in text
        or "what day is it today" in text
        or "what day is it" in text
    ):
        now = datetime.now()
        if LANG.startswith("vi"):
            return f"Hôm nay là ngày {now.day} tháng {now.month} năm {now.year}"
        return f"Today is {now.strftime('%B %d, %Y')}"

    # Không hiểu.
    if LANG.startswith("vi"):
        return "Tôi không hiểu, bạn thử nói lại nhé"
    return "I don't understand, please say it again"