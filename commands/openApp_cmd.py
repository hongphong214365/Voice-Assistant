import subprocess

def handle(text):
    if "mở" in text and "notepad" in text:
        subprocess.Popen(["notepad"])
        return "Đã mở notepad"
    return None