from transformers import pipeline
import logging

logging.basicConfig(filename='logs/app.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def transcribe_audio(audio_path):
    """Transcribe audio to English text using Whisper."""
    try:
        transcriber = pipeline("automatic-speech-recognition", model="openai/whisper-base")
        result = transcriber(audio_path)
        text = result["text"]
        logging.info(f"Transcribed audio {audio_path} to: {text[:50]}...")
        return text
    except Exception as e:
        logging.error(f"Transcription error: {e}")
        raise
