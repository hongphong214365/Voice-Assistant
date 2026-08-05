"""
File này chứa lệnh giúp trợ lí có thể mở các ứng dụng.
"""

import json
from pathlib import Path
import subprocess

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "apps.json"

with DATA_FILE.open(encoding="utf-8") as file:
    APPS = json.load(file)


def handle(text):
    if "mở" not in text:
        return None
    for name, exe in APPS.items():
        if name in text:
            subprocess.Popen([exe])
            return f"Đã mở {name}."
    return None
