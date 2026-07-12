"""
File này dùng để phát âm thanh khi bot đang nghe, nghe thành công, nghe thất bại.
"""

from pathlib import Path
import pygame
from config import AUDIO_DIR

pygame.mixer.init()

_audio_dir = Path(AUDIO_DIR)


def play(filename: str):
    """Phát 1 file trong thư mục audio"""
    path = _audio_dir / filename
    if not path.exists():
        return
    try:
        # Phát âm thanh.
        pygame.mixer.Sound(str(path)).play()
    except Exception:
        pass
