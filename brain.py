from commands import COMMANDS
from config import LANG


def think(text):
    text = text.lower()

    for command in COMMANDS:
        response = command.handle(text)
        if response:
            return response

    # Không hiểu.
    if LANG.startswith("vi"):
        return "Tôi không hiểu, bạn thử nói lại nhé"
    return "I don't understand, please say it again"
