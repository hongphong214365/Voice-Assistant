from datetime import datetime
from config import LANG
def handle(text):
    # hỏi ngày tháng năm
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
    return None