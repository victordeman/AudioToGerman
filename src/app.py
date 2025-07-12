import streamlit as st
import os
import logging
from audio_processor import extract_audio_from_video
from transcriber import transcribe_audio
from translator import translate_to_german
from text_to_speech import text_to_german_audio

# Configure logging
logging.basicConfig(filename='logs/app.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

st.title("AudioToGerman: Convert English Audio/Video to German Audio")

st.markdown("""
Upload an English audio (MP3, WAV) or video (MP4) file to transcribe it to English text, 
translate to German, and generate German audio. All processing is done offline.
""")

# File uploader
uploaded_file = st.file_uploader("Choose an audio or video file", type=["mp3", "wav", "mp4"])
is_video = st.checkbox("Input is a video file (MP4)")

# Process button
if st.button("Process File"):
    if uploaded_file is not None:
        try:
            # Save uploaded file
            input_path = os.path.join("input", uploaded_file.name)
            os.makedirs("input", exist_ok=True)
            with open(input_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.success(f"File {uploaded_file.name} uploaded successfully!")

            # Process file
            output_path = os.path.join("output", f"german_{uploaded_file.name.split('.')[0]}.wav")
            os.makedirs("output", exist_ok=True)
            
            with st.spinner("Processing... This may take a few minutes."):
                english_text, german_text, output_audio_path = process_media_to_german_audio(
                    input_path, output_path, is_video
                )
            
            # Display results
            st.subheader("Results")
            st.write("**English Transcription:**")
            st.write(english_text)
            st.write("**German Translation:**")
            st.write(german_text)
            st.write("**Generated German Audio:**")
            st.audio(output_audio_path)
            
            # Download button
            with open(output_audio_path, "rb") as f:
                st.download_button(
                    label="Download German Audio",
                    data=f,
                    file_name=os.path.basename(output_audio_path),
                    mime="audio/wav"
                )
            
            # Clean up input file
            os.remove(input_path)
            logging.info(f"Cleaned up uploaded file {input_path}")
            
        except Exception as e:
            st.error(f"Error: {str(e)}")
            logging.error(f"Streamlit processing error: {e}")
    else:
        st.error("Please upload a file.")

st.markdown("---")
st.write("Powered by Whisper, Opus-MT, and MMS-TTS. See [README](README.md) for details.")
