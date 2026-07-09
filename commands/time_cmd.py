from datetime import datetime
from config import LANG
def handle(text):

    # Hỏi giờ.
    if (
        "mấy giờ rồi" in text
        or "what time is it" in text
    ):
        now = datetime.now()
        if LANG.startswith("vi"):
            return f"Bây giờ là {now.hour} giờ {now.minute} phút"
        return f"It is {now.hour}:{now.minute:02d}"
    return None