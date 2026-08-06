import webbrowser
import json
from pathlib import Path
from config_error import handle_config_error

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "websites.json"
try:
    with DATA_FILE.open(encoding="utf-8") as file:
        SITES = json.load(file)
except (json.JSONDecodeError, FileNotFoundError) as error:
    handle_config_error(
        DATA_FILE.name,
        "mở website",
        error,
    )
    APPS = {}


def handle(text: str) -> str | None:
    if not text.startswith("mở "):
        return None

    name = text.removeprefix("mở ").strip()

    url = SITES.get(name)

    if not url:
        return None
    webbrowser.open(url)
    return f"Đã mở {name}"
