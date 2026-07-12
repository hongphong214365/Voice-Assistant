from config import STATE, LANG


def handle(text):
    if any(
        cmd in text
        for cmd in (
            "Tạm dừng nghe",
            "dừng nghe",
            "Ngừng  nghe",
            "stop listening",
        )
    ):
        STATE["LISTENING"] = False
        if LANG.startswith("vi"):
            return "Đã dừng nghe, ấn phím tắt để tiếp tục nghe."
        return "Stopped listening, press the shortcut to continue listening."
    return None
