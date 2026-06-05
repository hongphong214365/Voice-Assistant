# Python Voice Assistant

Simple voice assistant written in Python.

The assistant can listen through the microphone, convert speech to text, process simple commands, and reply using synthesized speech.

## Features

* Record audio from microphone.
* Convert speech to text.
* Reply with synthesized voice.
* Run continuously in a loop.
* Exit when the user says "tạm biệt".
* Simple command processing through a separate brain module.
* Modular project structure for future expansion.

## Requirements

* Python 3.11 or newer
* Microphone
* Internet connection (for speech recognition and gTTS)

## Project Structure

```text
assistant/

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
bạn tên gì
tạm biệt
```

#### speak.py

Handles:

* Text-to-speech generation
* Audio playback

## Install Dependencies

```bash
pip install sounddevice
pip install scipy
pip install SpeechRecognition
pip install gtts
pip install pygame-ce
```

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
```

Assistant:

```text
Chào bạn
```

### Ask Name

User:

```text
bạn tên gì vậy
```

Assistant:

```text
Tôi là trợ lí ảo của bạn
```

### Exit

User:

```text
tạm biệt
```

Assistant:

```text
Tạm biệt bạn
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
* Read current time.
* Read weather information.
* Wake word support.
* AI integration.

## Security Notes

Do not store passwords or sensitive information inside source code.

Keep API keys and tokens in environment variables whenever possible.

## License

MIT License
