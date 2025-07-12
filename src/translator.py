from transformers import pipeline
import logging

logging.basicConfig(filename='logs/app.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def translate_to_german(english_text):
    """Translate English text to German using Opus-MT."""
    try:
        translator = pipeline("translation_en_to_de", model="Helsinki-NLP/opus-mt-en-de")
        result = translator(english_text, max_length=400)
        german_text = result[0]["translation_text"]
        logging.info(f"Translated to German: {german_text[:50]}...")
        return german_text
    except Exception as e:
        logging.error(f"Translation error: {e}")
        raise
