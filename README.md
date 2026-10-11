# Trợ lý ảo bằng Python

Trợ lý ảo điều khiển bằng giọng nói đơn giản, hỗ trợ nhận diện và phản hồi giọng nói (Tiếng Việt và Tiếng Anh) trên hệ điều hành Windows.

[English version](README_en.md)

## Tính năng
* Hỗ trợ nhận diện và phản hồi bằng cả Tiếng Việt và Tiếng Anh.
* Điều khiển mở ứng dụng và website bằng giọng nói (dễ dàng tùy chỉnh).
* Hỗ trợ các câu lệnh cơ bản.
* Có thể thay đổi các âm báo khi trợ lí đang nghe, nghe thành công, nghe lỗi.
* Chuyển đổi ngôn ngữ dễ dàng.
* Dừng trợ lí **không thoát** có thể đánh thức bất cứ khi nào bằng phím tắt.
  
## Yêu cầu hệ thống
* Windows
* Python 3.11 hoặc mới hơn
* Micrô
* Kết nối Internet (để nhận dạng giọng nói và gTTS)

## Cài đặt thư viện
### Sử dụng uv (Khuyến nghị)

```bat
# Dùng môi trường venv
uv venv &&uv sync
# Nếu không:
uv sync
```
### Sử dụng pip
```bat
# Dùng venv:
python -m venv .venv
# Kích hoạt venv (PowerShell):
.\.venv\Scripts\activate.ps1
# Kích hoạt venv (CMD):
.venv\Scripts\activate.bat
# Cài đặt thư viện:
pip install -r requirements.txt
```
## Chạy trợ lý ảo

Sử dụng `uv` (Khuyến nghị):
```bash
uv run main.py
```

Sử dụng Python trực tiếp:
```bash
python main.py
```

*Khi khởi động thành công, trợ lý sẽ phát âm thanh và thông báo: "Chào bạn, tôi đã sẵn sàng".*

## Cấu hình

### 1. Cấu hình ngôn ngữ
Bạn có thể thay đổi ngôn ngữ của trợ lý trong file `config.py` bằng cách sửa biến `LANG`:
* Tiếng Việt: `LANG = "vi-VN"`
* Tiếng Anh: `LANG = "en-US"`

*Sau khi thay đổi ngôn ngữ, vui lòng khởi động lại trợ lý.*

### 2. Cấu hình trợ lý mở Website
Bạn có thể thêm hoặc sửa các website muốn trợ lý mở trong tệp `data/websites.json`.

Định dạng JSON phải theo đúng cấu trúc `"tên_gọi": "đường_link"`:
```json
{
  "google": "https://google.com",
  "youtube": "https://youtube.com",
  "facebook": "https://facebook.com",
  "face book": "https://facebook.com"
}
```
**Lưu ý:**
* **Tên gọi (Key):** Tên bạn nói với bot để mở website đó. Bạn có thể đặt tên tùy thích. Nếu không chắc chắn bot nhận diện chuẩn, bạn có thể gán nhiều tên gọi khác nhau cho cùng một link (ví dụ `"facebook"` và `"face book"`).
* **Đường link (Value):** Liên kết đến website. Nếu không chắc chắn link có đúng không, hãy copy chính xác từ thanh địa chỉ trình duyệt.
* Bạn có thể xóa bỏ các đường link mặc định có sẵn nếu không thích.

### 3. Cấu hình trợ lý mở Ứng dụng
Tương tự như website, bạn cấu hình các ứng dụng muốn mở trong tệp `data/apps.json`.

**Lưu ý:**
* Bạn phải biết và cung cấp **chính xác đường dẫn tuyệt đối** tới file thực thi `.exe` thì bot mới mở được.
* Cấu trúc JSON tương tự website. Lưu ý dùng dấu gạch chéo ngược kép `\\` (hoặc gạch chéo xuôi `/`) cho đường dẫn Windows.
* Có thể gán nhiều tên cho một ứng dụng và xóa các app mặc định.

Ví dụ:
```json
{
  "notepad": "C:\\Windows\\notepad.exe",
  "máy tính": "calc.exe",
  "ghi chú": "notepad.exe"
}
```

### 4. Bật chế độ Debug
Trong file `config.py`, bạn có thể sửa biến `DEBUG = True`. Khi cấu hình JSON bị sai định dạng hoặc xảy ra lỗi hệ thống, bot sẽ in chi tiết lỗi (traceback) ra màn hình console để bạn dễ theo dõi và sửa đổi.
### 5: Thay đổi âm thanh.
Nếu bạn không thích âm thanh mặc định của trợ lí. Bạn có thể đổi chúng bằng cách:
* Chuẩn bị file `.wav` của bạn. (Tốc độ lấy mẫu là: 44100.)
* Mở thư mục `audio` trong dự án.
* Tìm file bạn muốn thay thế:
    * `start.wav`: Âm thanh phát ra khi bot **bắt đầu lắng nghe** lệnh từ bạn.
    * `success.wav`: Âm thanh phát khi bot **nghe rõ câu lệnh và xử lí** lệnh của bạn.
    * `error.wav`: Âm thanh phát khi trợ lí **không thể nghe rõ** câu lệnh của bạn.
* Tiến hành thay thế bằng file của bạn.

### 6. Khôi phục file JSON mặc định
Nếu vô tình xóa hoặc sửa sai file JSON cấu hình, bạn có thể tải lại file gốc bị thiếu bằng cách vào repository dự án trên GitHub, mở thư mục `data/` và tải lại file tương ứng.

> [!IMPORTANT]
> Nếu file JSON bị sai định dạng cú pháp, bot sẽ tạm thời tắt tính năng đó. Để bật lại, vui lòng sửa lại file JSON cho đúng cấu trúc và khởi động lại trợ lí.

## Các lệnh hỗ trợ

### Xin chào
* **Người dùng:** `xin chào`
* **Trợ lý:** `Chào bạn`

### Hỏi tên
* **Người dùng:** `bạn tên gì` / `bạn tên gì vậy`
* **Trợ lý:** `Tôi là trợ lí ảo của bạn`

### Hỏi giờ
* **Người dùng:** `mấy giờ rồi`
* **Trợ lý:** `Bây giờ là [Giờ] giờ [Phút] phút`

### Hỏi ngày
* **Người dùng:** `hôm nay là ngày mấy` / `ngày bao nhiêu`
* **Trợ lý:** `Hôm nay là ngày...`

### Mở Website
* **Người dùng:** `mở google` / `mở youtube`
* **Trợ lý:** `Đã mở google` / `Đã mở youtube`

### Mở Ứng dụng
* **Người dùng:** `mở notepad` / `mở máy tính`
* **Trợ lý:** `Đã mở notepad.` / `Đã mở máy tính.`

### Tạm dừng nghe
* **Người dùng:** `tạm dừng nghe` / `dừng nghe`
* **Trợ lý:** `Đã dừng nghe, ấn phím tắt để tiếp tục nghe.` (Ấn phím tắt mặc định `Ctrl+Alt+A` để bật lại).

### Thoát
* **Người dùng:** `tạm biệt` / `kết thúc` / `bye` / `goodbye`
* **Trợ lý:** `Tạm biệt bạn, cần giúp gì thì nói mình nhé` (Sau đó chương trình sẽ tắt).

## Xử lý sự cố (Troubleshooting)

### Lỗi `No module named 'speech_recognition'`
Cài đặt bằng `uv` hoặc `pip`:
```bash
uv add SpeechRecognition
# hoặc
pip install SpeechRecognition
```

### Lỗi `No module named 'sounddevice'`
Cài đặt bằng `uv` hoặc `pip`:
```bash
uv add sounddevice
# hoặc
pip install sounddevice
```

### Lỗi `Permission denied: audio/Voice.mp3`
Tệp âm thanh có thể đang bị hệ thống/pygame khóa. Hãy đảm bảo pygame phát xong tệp âm thanh trước khi xóa hoặc tạo lại nó.

### Lỗi `UnknownValueError`
Trình nhận dạng giọng nói không hiểu được âm thanh. Hãy thử nói rõ ràng hơn, giảm tiếng ồn xung quanh hoặc tăng thời lượng ghi âm.

### Lỗi định dạng JSON (JSONDecodeError)
Nếu file cấu hình JSON bị lỗi cú pháp, chương trình sẽ báo dòng và cột bị lỗi.

**Một số lỗi JSON phổ biến và cách sửa:**

#### 1. Dư dấu phẩy ở phần tử cuối cùng
* **SAI:**
  ```json
  {
    "google": "https://google.com",
    "youtube": "https://youtube.com",
  }
  ```
* **ĐÚNG:**
  ```json
  {
    "google": "https://google.com",
    "youtube": "https://youtube.com"
  }
  ```

#### 2. Dùng sai dấu ngoặc kép (hoặc dùng ngoặc đơn)
* **SAI:**
  ```json
  {
    'google': 'https://google.com',
    notepad: "C:\\Windows\\notepad.exe"
  }
  ```
* **ĐÚNG:**
  ```json
  {
    "google": "https://google.com",
    "notepad": "C:\\Windows\\notepad.exe"
  }
  ```

#### 3. Thiếu dấu phẩy giữa các dòng
* **SAI:**
  ```json
  {
    "google": "https://google.com"
    "youtube": "https://youtube.com"
  }
  ```
* **ĐÚNG:**
  ```json
  {
    "google": "https://google.com",
    "youtube": "https://youtube.com"
  }
  ```

## Lưu ý bảo mật
* Chú ý tệp `record.wav`: File này chứa giọng nói thực tế của bạn ghi từ mic. Dự án đã bỏ qua nó trong `.gitignore`, nhưng hãy kiểm tra kỹ khi chỉnh sửa mã nguồn.
* Không lưu mật khẩu hoặc thông tin cá nhân trong mã nguồn. Hãy sử dụng biến môi trường khi cần dùng API key hoặc token.

## Giấy phép (License)
MIT License
