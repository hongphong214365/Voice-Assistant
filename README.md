# Trợ lý ảo bằng Python

Trợ lý ảo bằng giọng nói đơn giản được viết bằng Python.

Trợ lý có thể nghe qua micrô, chuyển giọng nói thành văn bản, xử lý các lệnh đơn giản và phản hồi bằng giọng nói tổng hợp.

[English version](README_en.md)

## Tính năng
* Hỗ trợ các lệnh cơ bản bằng tiếng Anh.
* Cấu hình cài đặt ngôn ngữ.
* Ghi âm âm thanh từ micrô.
* Chuyển giọng nói thành văn bản.
* Phản hồi bằng giọng nói tổng hợp.
* Chạy liên tục trong một vòng lặp.
* Thoát khi người dùng nói "tạm biệt".
* Xử lý các lệnh đơn giản thông qua một mô-đun brain riêng biệt.
* Cấu trúc dự án dạng mô-đun để dễ dàng mở rộng trong tương lai.

## Yêu cầu hệ thống
* Windows 
* Python 3.11 hoặc mới hơn
* Micrô
* Kết nối Internet (để nhận dạng giọng nói và gTTS)

## Cấu trúc dự án

```text
assistant/
│
├── audio/            # Lưu các tệp âm thanh tạm thời
├── commands/         # Bộ xử lý các lệnh tùy chỉnh
│   ├── __init__.py
│   ├── date_cmd.py
│   ├── greeting_cmd.py
│   ├── listening_cmd.py
│   ├── openApp_cmd.py
│   ├── openWeb_cmd.py
│   └── time_cmd.py
│
├── listen.py         # Mô-đun chuyển giọng nói thành văn bản (STT)
├── brain.py          # Bộ điều phối logic
├── speak.py          # Mô-đun chuyển văn bản thành giọng nói (TTS)
├── main.py           # Điểm khởi chạy ứng dụng
├── config.py         # Cấu hình ngôn ngữ và các tham số
└── README.md
```

### Mô tả tệp tin

#### main.py

Điểm khởi chạy chính.

Điều phối luồng công việc của trợ lý:

```text
Listen (Nghe) -> Think (Nghĩ) -> Speak (Nói)
```

#### listen.py

Xử lý:

* Ghi âm âm thanh
* Nhận dạng giọng nói

#### brain.py

Xử lý:

* Xử lý lệnh
* Tạo phản hồi

Ví dụ:

```text
xin chào
Hello
bạn tên gì
Mấy giờ rồi?
what time is it
tạm biệt
good bye
```

#### speak.py

Xử lý:

* Tạo giọng nói tổng hợp từ văn bản
* Phát lại âm thanh

## Cài đặt các thư viện phụ thuộc

### Sử dụng uv (Được khuyến nghị)
Dự án này được cấu hình với `uv`. Để chạy hoặc thêm các thư viện phụ thuộc:
```bash
# Thêm một thư viện
uv add <package_name>
```

### Sử dụng pip
```bash
pip install -r requirements.txt
```

## Cấu hình

Ngôn ngữ của trợ lý có thể được thay đổi trong:

```python
# config.py
LANG = "vi-VN"
```

Ví dụ:

```python
LANG = "vi-VN"
```

Tiếng Việt

```python
LANG = "en-US"
```

Tiếng Anh

Sau khi thay đổi ngôn ngữ, hãy khởi động lại trợ lý.

## Chạy trợ lý ảo

Sử dụng `uv` (Được khuyến nghị):
```bash
uv run main.py
```

Sử dụng Python trực tiếp:
```bash
python main.py
```

Ví dụ:

```text
Tôi đang nghe đây
đang nhận diện
```

## Các lệnh hỗ trợ

### Xin chào (Greeting)

Người dùng:

```text
xin chào
hello
```

Trợ lý:

```text
Chào bạn
hello
```

### Hỏi tên (Ask Name)

Người dùng:

```text
bạn tên gì vậy
bạn tên gì
what is your name
what's your name
```

Trợ lý:

```text
Tôi là trợ lí ảo của bạn
I am your virtual assistant
```

### Hỏi giờ (Ask Time)

Người dùng:

```text
mấy giờ rồi
what time is it
```

Trợ lý:

```text
Bây giờ là 17 giờ 5 phút
It is 17:05
```

### Hỏi ngày (Ask Date)

Người dùng:

```text
hôm nay là ngày mấy
ngày mấy
ngày bao nhiêu
what is today's date
what's today's date
what is the date today
what's the date
what day is it today
what day is it
```

Trợ lý:

```text
Hôm nay là ngày 15 tháng 6 năm 2026
Today is June 15, 2026
```

### Mở Website (Open Website)

Người dùng:
```text
mở google
mở youtube
mở github
mở git hub
mở gmail
```

Trợ lý:
```text
Đã mở google
Đã mở youtube
Đã mở github
Đã mở git hub
Đã mở gmail
```

### Mở ứng dụng (Open Application)

Người dùng:
```text
mở notepad
mở ghi chú
mở máy tính
mở calculator
mở file explorer
```

Trợ lý:
```text
Đã mở notepad.
Đã mở ghi chú.
Đã mở máy tính.
Đã mở calculator.
Đã mở file explorer.
```

### Tạm dừng nghe (Stop Listening)

Người dùng:
```text
tạm dừng nghe
dừng nghe
ngừng nghe
stop listening
```

Trợ lý:
```text
Đã dừng nghe, ấn phím tắt để tiếp tục nghe.
Stopped listening, press the shortcut to continue listening.
```

### Thoát (Exit)

Người dùng:

```text
tạm biệt bạn
bye
kết thúc
tạm biệt
thoát
good bye
goodbye
```

Trợ lý:

```text
Tạm biệt bạn, cần giúp gì thì nói mình nhé
good bye
```

Sau đó chương trình sẽ kết thúc.

## Xử lý sự cố (Troubleshooting)

### Lỗi No module named 'speech_recognition'

Cài đặt:

```bash
pip install SpeechRecognition
```

### Lỗi No module named 'sounddevice'

Cài đặt:

```bash
pip install sounddevice
```

### Lỗi Permission denied: audio/Voice.mp3

Tệp âm thanh có thể vẫn đang được sử dụng.

Đảm bảo pygame đã phát xong tệp âm thanh trước khi xóa hoặc tạo lại nó.

### Lỗi UnknownValueError

Trình nhận dạng giọng nói không thể hiểu được âm thanh.

Hãy thử:

* Nói rõ ràng hơn
* Giảm tiếng ồn xung quanh
* Tăng thời lượng ghi âm

## Kế hoạch tương lai

* Đọc thông tin thời tiết.
* Hỗ trợ từ kích hoạt (Wake word).
* Tích hợp AI.

## Lưu ý bảo mật

Không lưu trữ mật khẩu hoặc thông tin nhạy cảm trong mã nguồn.

Hãy lưu các khóa API và mã thông báo (token) trong các biến môi trường bất cứ khi nào có thể.

## Giấy phép (License)

MIT License
