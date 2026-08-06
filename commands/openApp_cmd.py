"""
File này chứa lệnh giúp trợ lí có thể mở các ứng dụng.
"""

import json
from pathlib import Path
import subprocess
from config_error import handle_config_error

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "apps.json"
try:
    with DATA_FILE.open(encoding="utf-8") as file:
        APPS = json.load(file)
except (json.JSONDecodeError, FileNotFoundError) as error:
    handle_config_error(
        DATA_FILE.name,
        "mở app",
        error,
    )
    APPS = {}


def handle(text):
    if "mở" not in text:
        return None
    for name, exe in APPS.items():
        if name in text:
            subprocess.Popen([exe])
            return f"Đã mở {name}."
    return None
