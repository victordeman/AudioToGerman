# AudioToGerman

A Python project to extract English text from audio/video, translate it to German, and generate German audio, all offline, with a Streamlit web interface.

## Features
- Extracts audio from video (MP4) or uses audio (MP3, WAV).
- Transcribes English audio to text using Whisper.
- Translates English text to German using Opus-MT.
- Converts German text to audio using MMS-TTS.
- Streamlit UI for file upload, processing, and result download.
- Fully offline, no API keys required.

## Requirements
- Python 3.8–3.11
- FFmpeg (system-wide installation)
- CPU (GPU recommended for faster processing)

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/victordeman/AudioToGerman
   cd AudioToGerman
