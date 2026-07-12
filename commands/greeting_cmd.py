from config import LANG


def handle(text):

    # Xin chào.
    if "xin chào" in text or "hello" in text:
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
    return None
