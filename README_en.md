# Python Voice Assistant

A simple voice-controlled assistant that supports speech recognition and response (Vietnamese and English) on Windows OS.

[Bản tiếng Việt](README.md)

## Features
* Supports recognition and response in both Vietnamese and English.
* Controls and opens applications/websites using voice commands (easily customizable).
* Records audio from microphone and converts speech to text (STT).
* Responds using synthesized speech (TTS).
* Runs continuously in a loop, automatically pausing or exiting when command is received.

## Requirements
* Windows
* Python 3.11 or newer
* Microphone
* Internet connection (for speech recognition and gTTS)

## Install Dependencies

### Using uv (Recommended)
```bash
uv sync
```

### Using pip
```bash
pip install -r requirements.txt
```

## Running The Assistant

Using `uv` (Recommended):
```bash
uv run main.py
```

Using Python directly:
```bash
python main.py
```
*Upon successful startup, the assistant will play a notification sound and announce: "Chào bạn, tôi đã sẵn sàng" (or "Hello, I'm ready" if the language is configured to English).*

## Configuration

### 1. Language Configuration
You can change the assistant's language in the `config.py` file by editing the `LANG` variable:
* Vietnamese: `LANG = "vi-VN"`
* English: `LANG = "en-US"`

*After changing the language, please restart the assistant.*

### 2. Configure Assistant to Open Websites
You can add or modify the websites you want the assistant to open in the `data/websites.json` file.

The JSON format must strictly follow the `"name": "link"` key-value structure:
```json
{
  "google": "https://google.com",
  "youtube": "https://youtube.com",
  "facebook": "https://facebook.com",
  "face book": "https://facebook.com"
}
```
**Notes:**
* **Name (Key):** The name you say to the bot to open that website. You can name it whatever you like. If you're concerned about the bot misinterpreting your pronunciation, you can assign multiple names to the same link (e.g. `"facebook"` and `"face book"` as shown above).
* **Link (Value):** The URL to the website. If you are not sure if the link is correct, access the website using your browser and copy the exact URL from the address bar.
* You can delete default links if you don't use them.

### 3. Configure Assistant to Open Applications
Similar to websites, you can configure the applications you want to open in the `data/apps.json` file.

**Notes:**
* You must provide the **exact absolute path** to the executable file (`.exe`) of the application so that the bot can open it.
* The JSON structure is identical to websites. Note that you should use double backslashes `\\` (or forward slashes `/`) for Windows paths.
* You can assign multiple names to a single application and delete unnecessary default apps.

Example:
```json
{
  "notepad": "C:\\Windows\\notepad.exe",
  "calculator": "calc.exe",
  "notes": "notepad.exe"
}
```

### 4. Enable Debug Mode
In the `config.py` file, you can set `DEBUG = True`. If a JSON configuration is malformed or a system error occurs, the bot will print the detailed traceback (error stack) to the console to help you easily locate and fix the issue.

### 5. Restore Default JSON Files
If you accidentally delete or break the format of a JSON configuration file, you can restore it by visiting the project repository on GitHub, navigating to the `data/` directory, and downloading the corresponding default file.

> [!IMPORTANT]
> If a JSON file is syntactically invalid, the bot will temporarily disable that specific feature. To reactivate it, please fix the JSON file and restart the bot.

## Supported Commands

### Greeting
* **User:** `xin chào` / `hello`
* **Assistant:** `Chào bạn` / `hello`

### Ask Name
* **User:** `bạn tên gì` / `bạn tên gì vậy` / `what is your name`
* **Assistant:** `Tôi là trợ lí ảo của bạn` / `I am your virtual assistant`

### Ask Time
* **User:** `mấy giờ rồi` / `what time is it`
* **Assistant:** `Bây giờ là [Hour] giờ [Minute] phút` / `It is [Hour]:[Minute]`

### Ask Date
* **User:** `hôm nay là ngày mấy` / `ngày bao nhiêu` / `what day is it today`
* **Assistant:** `Hôm nay là ngày...` / `Today is...`

### Open Website
* **User:** `mở google` / `mở youtube`
* **Assistant:** `Đã mở google` / `Đã mở youtube`

### Open Application
* **User:** `mở notepad` / `mở máy tính`
* **Assistant:** `Đã mở notepad.` / `Đã mở máy tính.`

### Stop Listening
* **User:** `tạm dừng nghe` / `dừng nghe` / `stop listening`
* **Assistant:** `Đã dừng nghe, ấn phím tắt để tiếp tục nghe.` (Press the default hotkey `Ctrl+Alt+A` to resume listening).

### Exit
* **User:** `tạm biệt` / `kết thúc` / `bye` / `goodbye`
* **Assistant:** `Tạm biệt bạn, cần giúp gì thì nói mình nhé` / `good bye` (The program will then exit).

## Troubleshooting

### Error `No module named 'speech_recognition'`
Install using `uv` or `pip`:
```bash
uv add SpeechRecognition
# or
pip install SpeechRecognition
```

### Error `No module named 'sounddevice'`
Install using `uv` or `pip`:
```bash
uv add sounddevice
# or
pip install sounddevice
```

### Error `Permission denied: audio/Voice.mp3`
The audio file may still be locked by the system/pygame. Make sure pygame has finished playing the file before deleting or recreating it.

### Error `UnknownValueError`
The speech recognizer could not understand the audio. Try speaking more clearly, reducing background noise, or increasing the recording duration.

### JSON Format Error (JSONDecodeError)
If a JSON configuration file has syntax errors, the program will output the line and column number where the error occurred.

**Common JSON errors and how to fix them:**

#### 1. Trailing comma in the last element
* **INCORRECT:**
  ```json
  {
    "google": "https://google.com",
    "youtube": "https://youtube.com",
  }
  ```
* **CORRECT:**
  ```json
  {
    "google": "https://google.com",
    "youtube": "https://youtube.com"
  }
  ```

#### 2. Incorrect quote marks (or single quotes)
* **INCORRECT:**
  ```json
  {
    'google': 'https://google.com',
    notepad: "C:\\Windows\\notepad.exe"
  }
  ```
* **CORRECT:**
  ```json
  {
    "google": "https://google.com",
    "notepad": "C:\\Windows\\notepad.exe"
  }
  ```

#### 3. Missing comma between elements
* **INCORRECT:**
  ```json
  {
    "google": "https://google.com"
    "youtube": "https://youtube.com"
  }
  ```
* **CORRECT:**
  ```json
  {
    "google": "https://google.com",
    "youtube": "https://youtube.com"
  }
  ```

## Security Notes
* Keep an eye on `record.wav`: This file contains your actual voice recorded from the mic. It is ignored by `.gitignore` by default, but double-check it when modifying source code.
* Do not store passwords or personal information in the source code. Use environment variables when API keys or tokens are needed.

## License
MIT License
