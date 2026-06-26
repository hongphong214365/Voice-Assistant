import webbrowser

# Danh sách website, có thể mở rộng.
SITES = {
    "google": "https://google.com",
    "youtube": "https://www.youtube.com",
    "gmail": "https://mail.google.com",
    "github": "https://github.com",
    "git hub": "https://github.com",
}

# Hàm xử lí.
def handle(text: str) -> str | None:
    if not text.statswith("mở "):
        return None

    name = text.removeprefix("mở ").strip():

    url = SITES.get(name)

    if not url:
        return None
    webbrowser(url)