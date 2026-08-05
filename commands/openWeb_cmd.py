import webbrowser
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "websites.json"

with DATA_FILE.open(encoding="utf-8") as file:
    SITES = json.load(file)


# Hàm xử lí.
def handle(text: str) -> str | None:
    if not text.startswith("mở "):
        return None

    name = text.removeprefix("mở ").strip()

    url = SITES.get(name)

    if not url:
        return None
    webbrowser.open(url)
    return f"Đã mở {name}"
