# Kế hoạch dài hạn: Dynamic Audio

## Mục tiêu

Trợ lý thu giọng nói theo thời gian thực, tự nhận biết lúc bắt đầu và kết thúc câu, giữ âm đầu/cuối, xử lý im lặng và giới hạn thời lượng. Audio chỉ được giữ trong RAM; `listen.py` điều phối microphone và nhận dạng, còn thuật toán tín hiệu nằm trong `audio_processor.py`. Giao diện `listen()` và luồng `brain.py` được giữ ổn định.

VAD tự xây dựng bằng NumPy là bộ phát hiện dựa trên năng lượng, không cam kết phân biệt hoàn hảo giọng nói với mọi tiếng ồn. Không thêm thư viện VAD bên ngoài nếu chưa có yêu cầu thực tế chứng minh cần thiết.

## Kiến trúc đích

```text
main.py -> listen.py -> sounddevice InputStream
                       -> audio_processor.py (đo tín hiệu, VAD, buffer)
                       -> SpeechRecognition AudioData -> Google STT
```

`audio_processor.py` nhận các block NumPy và trả kết quả có ý nghĩa; `listen.py` không tự triển khai phép tính tín hiệu. Cấu hình thời gian và ngưỡng đặt tập trung trong `config.py` khi các giá trị được tích hợp vào luồng sử dụng thật.

## Lộ trình và tiêu chí hoàn tất

### 1. Nền tảng phép đo

- Tạo `audio_processor.py` độc lập với microphone.
- RMS trả về mức hiệu dụng theo đơn vị dữ liệu đầu vào; tránh tràn số khi bình phương mẫu int16.
- Peak trả về biên độ tuyệt đối lớn nhất; xử lý đúng cả mẫu âm nhỏ nhất của int16.
- Kiểm tra dữ liệu rỗng, kiểu dữ liệu và các dạng mảng thường gặp.
- Viết unit test chạy không cần microphone hoặc mạng.

**Hoàn tất khi:** phép đo có kiểm thử xác định cho tín hiệu im lặng, hằng, âm/ dương, dữ liệu int16 biên và đầu vào không hợp lệ.

### 2. VAD cơ bản và trạng thái

- Định nghĩa trạng thái chờ nói, đang ghi và kết thúc câu.
- Bắt đầu nói theo ngưỡng RMS cao hơn; tiếp tục nói theo ngưỡng thấp hơn (hysteresis).
- Đếm thời lượng im lặng bằng thời gian hoặc số mẫu nhất quán, không phụ thuộc độ trễ vòng lặp.
- Không cập nhật noise floor khi đang nói.

**Hoàn tất khi:** test bao phủ chuyển trạng thái, dao động quanh ngưỡng, khoảng lặng ngắn và kết thúc sau khoảng lặng đủ dài.

### 3. Ngưỡng tiếng ồn thích nghi

- Ước lượng noise floor trong giai đoạn hiệu chỉnh giới hạn thời gian.
- Cập nhật chậm khi không phát hiện giọng nói; chặn giá trị tối thiểu/tối đa hợp lý.
- Tính ngưỡng bắt đầu/tiếp tục từ noise floor cùng margin/factor có thể cấu hình.
- Bảo đảm tiếng ồn nền ổn định không làm trợ lý thu vô hạn.

**Hoàn tất khi:** test mô phỏng nền yên, nền ồn hơn và tiếng nói không bị noise floor đuổi theo.

### 4. Buffer và giới hạn phiên

- Pre-roll giữ khoảng 200–300 ms trước lúc phát hiện nói.
- Giữ đoạn im lặng cuối đủ để không cắt âm cuối; bỏ phần im lặng vượt ngưỡng kết thúc.
- Thời lượng tối thiểu loại bỏ đoạn nhiễu rất ngắn.
- No-speech timeout trả `None`; maximum duration chốt câu dài để chuyển nhận dạng.
- Giới hạn bộ nhớ theo thời lượng tối đa và sample rate.

**Hoàn tất khi:** test kiểm tra số mẫu pre-roll, silence tail, timeout và giới hạn thời lượng.

### 5. Tích hợp microphone và nhận dạng

- `listen.py` đọc block nhỏ, chuyển dữ liệu qua processor, ghép đúng thứ tự trong RAM.
- Tạo `sr.AudioData` với sample rate và sample width tương ứng dữ liệu thực tế.
- Giữ cách xử lý lỗi thiết bị, overflow, lỗi Google và hành vi trả `None`.
- Không tạo WAV tạm; không đổi giao diện gọi từ `main.py`/`brain.py`.

**Hoàn tất khi:** unit test giả lập stream/processor bao phủ lỗi và kết thúc câu; kiểm tra thủ công với microphone khi có thiết bị.

### 6. Kiểm chứng và tinh chỉnh

- Kiểm thử nói nhỏ/lớn, câu dài, ngắt giữa câu, nền quạt, không nói, tiếng động sau câu.
- Ghi nhận false positive/false negative và điều chỉnh mặc định dựa trên mẫu thực tế.
- Chạy `uv format`, `uv check` và toàn bộ unit test trước khi tích hợp.
- Không xem phép đo RMS/Peak đơn thuần là phân loại giọng nói; tiếp tục cải thiện theo dữ liệu thực.

## Thứ tự triển khai

Tiến hành từng lát cắt có thể kiểm thử độc lập: phép đo RMS/Peak, VAD/hysteresis, hiệu chỉnh nền, buffer/timeout, rồi tích hợp microphone. Mỗi lát cắt cần có test trước khi mở rộng sang bước kế tiếp. Các giá trị ban đầu (block 100 ms, silence 0,8 s, pre-roll 250 ms, tối đa 15 s, chờ nói 5 s) chỉ là cấu hình khởi điểm và cần được xác nhận trên microphone thực.

## Tình trạng

- [x] Nền streaming hiện tại dùng `InputStream` và xử lý audio trong RAM.
- [ ] RMS và Peak độc lập, có unit test.
- [ ] VAD cơ bản, hysteresis và kết thúc theo im lặng.
- [ ] Noise floor thích nghi.
- [ ] Pre-roll, giới hạn tối thiểu/tối đa và timeout.
- [ ] Tích hợp đầy đủ với `listen.py` và kiểm thử microphone thực.
