from datetime import datetime
def think(text):
    text = text.lower()

    if "xin chào" in text:
        return "Chào bạn"
    if "bạn tên gì vậy" in text:
        return "Tôi là trợ lí ảo của bạn"
    if "mấy giờ rồi" or "Giờ là mấy giờ" in text:
        now = datetime.now()
        return f"Bây giờ là {now.hour} giờ {now.minute} phút"
    else:
        return "Tôi không hiểu, bạn thử nói lại nhé"