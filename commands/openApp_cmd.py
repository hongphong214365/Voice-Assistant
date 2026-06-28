import subprocess

APPS = {
    "notepad": "notepad.exe",
    "ghi chú": "notepad.exe",
    "máy tính": "calc.exe",
    "calculator": "calc.exe",
    "file explorer": "explorer.exe"
}
    
def handle(text):
    if "mở" not in text:
        return None
    for name, exe in APPS.items():
        if name in text:
            subprocess.Popen([exe])
            return f"Đã mở {name}."
    return None