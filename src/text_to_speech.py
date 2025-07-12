from transformers import VitsModel, AutoTokenizer
import torch
import scipy
import logging
import os

logging.basicConfig(filename='logs/app.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def text_to_german_audio(german_text, output_audio_path):
    """Convert German text to audio using MMS-TTS."""
    try:
        model = VitsModel.from_pretrained("facebook/mms-tts-deu")
        tokenizer = AutoTokenizer.from_pretrained("facebook/mms-tts-deu")
        inputs = tokenizer(german_text, return_tensors="pt")
        with torch.no_grad():
            output = model(**inputs).waveform
        scipy.io.wavfile.write(output_audio_path, rate=model.config.sampling_rate, 
                              data=output.squeeze().numpy())
        logging.info(f"Generated German audio at {output_audio_path}")
        return output_audio_path
    except Exception as e:
        logging.error(f"Text-to-speech error: {e}")
        raise
