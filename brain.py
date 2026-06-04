def think(text):
    text = text.lower()

    if "xin chào" in text:
        return "Chào bạn"
    if "bạn tên gì vậy" in text:
        return "Tôi là trợ lí ảo của bạn"
    else:
        return "Tôi không hiểu, bạn thử nói lại nhé"