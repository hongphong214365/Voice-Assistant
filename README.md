# Python Voice Assistant

Simple voice assistant written in Python.

The assistant can listen through the microphone, convert speech to text, process simple commands, and reply using synthesized speech.

## Features
* Basic English command support.
* Configurable language setting.
* Record audio from microphone.
* Convert speech to text.
* Reply with synthesized voice.
* Run continuously in a loop.
* Exit when the user says "tạm biệt".
* Simple command processing through a separate brain module.
* Modular project structure for future expansion.

## Requirements
* Windows 
* Python 3.11 or newer
* Microphone
* Internet connection (for speech recognition and gTTS)

## Project Structure

```text
assistant/
├── config.py
├── main.py
├── listen.py
├── brain.py
├── speak.py
└── audio/
```

### File Description

#### main.py

Main entry point.

Controls the assistant workflow:

```text
Listen -> Think -> Speak
```

#### listen.py

Handles:

* Audio recording
* Speech recognition

#### brain.py

Handles:

* Command processing
* Response generation

Examples:

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

Handles:

* Text-to-speech generation
* Audio playback

## Install Dependencies
```bash
pip install -r requirements.txt
```
or
```bash
pip install sounddevice
pip install scipy
pip install SpeechRecognition
pip install gtts
pip install pygame-ce
```

## Configuration

The assistant language can be changed in:

```python
# config.py
LANG = "vi-VN"
```

Examples:

```python
LANG = "vi-VN"
```

Vietnamese

```python
LANG = "en-US"
```

English

After changing the language, restart the assistant.

## Running The Assistant

Open a terminal inside the project folder:

```bash
python main.py
```

Example:

```text
Tôi đang nghe đây
đang nhận diện
```

## Supported Commands

### Greeting

User:

```text
xin chào
hello
```

Assistant:

```text
Chào bạn
```

### Ask Name

User:

```text
bạn tên gì vậy
bạn tên gì
what is your name
what's your name
```

Assistant:

```text
Tôi là trợ lí ảo của bạn
I am your virtual assistant
```

### Ask Time

User:

```text
mấy giờ rồi
what time is it
```

Assistant:

```text
Bây giờ là 17 giờ 5 phút
It is 17:05
```

### Ask Date

User:

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

Assistant:

```text
Hôm nay là ngày 15 tháng 6 năm 2026
Today is June 15, 2026
```

### Exit

User:

```text
tạm biệt bạn
bye
kết thúc
tạm biệt
thoát
good bye
goodbye
```

Assistant:

```text
Tạm biệt bạn, cần giúp gì thì nói mình nhé
good bye
```

The program will then exit.

## Troubleshooting

### No module named 'speech_recognition'

Install:

```bash
pip install SpeechRecognition
```

### No module named 'sounddevice'

Install:

```bash
pip install sounddevice
```

### Permission denied: audio/Voice.mp3

The audio file may still be in use.

Make sure pygame has finished playing the file before deleting or recreating it.

### UnknownValueError

Speech recognition could not understand the audio.

Try:

* Speaking more clearly
* Reducing background noise
* Increasing recording duration

## Future Plans

* Open applications by voice.
* Search Google.
* Read weather information.
* Wake word support.
* AI integration.

## Security Notes

Do not store passwords or sensitive information inside source code.

Keep API keys and tokens in environment variables whenever possible.

## License

MIT License
