import keyboard
from config import STATE, START_SOUND
from sound import play


def wake_up():

    if STATE["LISTENING"]:
        return
    STATE["LISTENING"] = True
    # Phát âm thanh.
    play(START_SOUND)


def register_hotkeys():
    keyboard.add_hotkey("ctrl+alt+a", wake_up)
