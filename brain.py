from datetime import datetime
def think(text):
    text = text.lower()

    # Xin chào.
    if "xin chào" in text:
        return "Chào bạn"
    # Hỏi tên.
    if "bạn tên gì vậy" in text:
        return "Tôi là trợ lí ảo của bạn"
    # Hỏi giờ.
    if (
        "mấy giờ rồi" in text
        or "giờ là mấy giờ" in text
    ):
        now = datetime.now()
        return f"Bây giờ là {now.hour} giờ {now.minute} phút"
    else:
        return "Tôi không hiểu, bạn thử nói lại nhé"