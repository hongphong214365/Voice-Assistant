import math
import struct
import wave
import sys
from pathlib import Path
import pygame

# ==========================
# Cấu hình & Khởi tạo
# ==========================
SAMPLE_RATE = 44100
BASE_DIR = Path(__file__).resolve().parent.parent
AUDIO_DIR = BASE_DIR / "audio"
AUDIO_DIR.mkdir(exist_ok=True)

if not pygame.mixer.get_init():
    pygame.mixer.init(frequency=SAMPLE_RATE, size=-16, channels=1)


# ==========================
# Các hàm Core
# ==========================
def append_tone(
    frames, frequency, duration, volume=0.25
):  # Giảm volume xuống chút cho đỡ chói tai
    total_samples = int(SAMPLE_RATE * duration)
    for i in range(total_samples):
        sample = volume * math.sin(2 * math.pi * frequency * i / SAMPLE_RATE)
        value = int(sample * 32767)
        frames.append(struct.pack("<h", value))


def append_sweep(frames, start_freq, end_freq, duration, volume=0.25):
    total_samples = int(SAMPLE_RATE * duration)
    for i in range(total_samples):
        frequency = start_freq + ((end_freq - start_freq) * i / total_samples)
        sample = volume * math.sin(2 * math.pi * frequency * i / SAMPLE_RATE)
        value = int(sample * 32767)
        frames.append(struct.pack("<h", value))


def save_and_play(filename, frames):
    file_path = AUDIO_DIR / filename
    with wave.open(str(file_path), "wb") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(SAMPLE_RATE)
        wav.writeframes(b"".join(frames))

    pygame.mixer.stop()
    sound = pygame.mixer.Sound(str(file_path))
    sound.play()


# ==========================
# Khởi tạo tham số mặc định của bạn
# ==========================
start_f1, start_f2 = 650, 800
success_f1, success_f2 = 900, 1200
error_f1, error_f2 = 500, 250

step = 50  # Mỗi lần tăng giảm 50Hz

while True:
    print("\n" + "=" * 40)
    print(f" PHÒNG LAB THẨM M - TẦN SỐ HIỆN TẠI:")
    print(f"  [1] Start:   {start_f1}Hz -> {start_f2}Hz")
    print(f"  [2] Success: {success_f1}Hz -> {success_f2}Hz")
    print(f"  [3] Error:   {error_f1}Hz -> {error_f2}Hz")
    print("=" * 40)
    print(" [1/2/3] Nghe thử file tương ứng")
    print(" [+ / -] Tăng / Giảm tần số của file vừa nghe")
    print(" [q]     Thoát và chốt cấu hình")
    print("=" * 40)

    choice = input("Nhập lệnh (Ví dụ: 1 hoặc + hoặc -): ").strip().lower()

    # Lưu lại file vừa chọn gần nhất để tăng giảm cho đúng mục tiêu
    if choice in ["1", "2", "3"]:
        last_selected = choice

    if choice == "1":
        frames = []
        append_tone(frames, start_f1, 0.1)
        append_tone(frames, start_f2, 0.1)
        save_and_play("start.wav", frames)

    elif choice == "2":
        frames = []
        append_tone(frames, success_f1, 0.05)
        append_tone(frames, success_f2, 0.05)
        save_and_play("success.wav", frames)

    elif choice == "3":
        frames = []
        append_sweep(frames, error_f1, error_f2, 0.18)
        save_and_play("error.wav", frames)

    elif choice == "+":
        if last_selected == "1":
            start_f1 += step
            start_f2 += step
        elif last_selected == "2":
            success_f1 += step
            success_f2 += step
        elif last_selected == "3":
            error_f1 += step
            error_f2 += step
        print(f"[+] Đã tăng tần số. Hãy bấm nút [{last_selected}] để nghe lại.")

    elif choice == "-":
        if last_selected == "1":
            start_f1 -= step
            start_f2 -= step
        elif last_selected == "2":
            success_f1 -= step
            success_f2 -= step
        elif last_selected == "3":
            error_f1 -= step
            error_f2 -= step
        print(f"[-] Đã giảm tần số. Hãy bấm nút [{last_selected}] để nghe lại.")

    elif choice == "q":
        print("\n>>> CẤU HÌNH CUỐI CÙNG CỦA BẠN (Copy lại mang vào code chính):")
        print(f"Start: {start_f1}, {start_f2}")
        print(f"Success: {success_f1}, {success_f2}")
        print(f"Error: {error_f1}, {error_f2}")
        pygame.quit()
        sys.exit()
