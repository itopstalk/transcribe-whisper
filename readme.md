This repo holds a sample script that allows you to transcribe all the MP3 files in the specified directory into text using OpenAI's Whisper tool

To set up your Windows Subsystem for Linux distribution (assuming the default Ubuntu installation with wsl.exe --install) run the following commands (which install the necessary python bits, the openai whisper bits, and the ffmpeg transcoding software)

```wsl.exe
- sudo apt install python3-pip
- pip install openai-whisper
- sudo apt install ffmpeg
```

Once you've got the prerequsites installed, you can use the transcribe.py file in this repo by running the command:

```wsl
python3 transcribe.py
```

If you have files in another format, you can either update the script or convert using: 

```wsl
ffmpeg -i filename.wav filename.mp3
```
