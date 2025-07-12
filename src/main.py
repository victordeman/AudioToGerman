import argparse
import os
import logging
from audio_processor import extract_audio_from_video
from transcriber import transcribe_audio
from translator import translate_to_german
from text_to_speech import text_to_german_audio

logging.basicConfig(filename='logs/app.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def process_media_to_german_audio(input_path, output_audio_path, is_video=False):
    """Process media file to generate German audio."""
    try:
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Input file {input_path} not found")
        audio_path = "input/temp_audio.mp3" if is_video else input_path
        if is_video:
            extract_audio_from_video(input_path, audio_path)
        english_text = transcribe_audio(audio_path)
        print(f"English Transcription: {english_text}")
        german_text = translate_to_german(english_text)
        print(f"German Translation: {german_text}")
        text_to_german_audio(german_text, output_audio_path)
        print(f"German audio saved as {output_audio_path}")
        if is_video and os.path.exists(audio_path):
            os.remove(audio_path)
            logging.info(f"Cleaned up temporary file {audio_path}")
        return english_text, german_text, output_audio_path
    except Exception as e:
        logging.error(f"Processing error: {e}")
        raise

def main():
    parser = argparse.ArgumentParser(description="Convert English audio/video to German audio.")
    parser.add_argument("--input", required=True, help="Path to input audio/video file")
    parser.add_argument("--output", required=True, help="Path to output German audio file")
    parser.add_argument("--is-video", action="store_true", help="Flag if input is a video file")
    args = parser.parse_args()
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    process_media_to_german_audio(args.input, args.output, args.is_video)

if __name__ == "__main__":
    main()
