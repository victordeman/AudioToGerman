import ffmpeg
import logging
import os

logging.basicConfig(filename='logs/app.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def extract_audio_from_video(video_path, audio_path):
    """Extract audio from a video file using FFmpeg."""
    try:
        if not os.path.exists(video_path):
            raise FileNotFoundError(f"Video file {video_path} not found")
        stream = ffmpeg.input(video_path)
        stream = ffmpeg.output(stream, audio_path, format='mp3', acodec='mp3')
        ffmpeg.run(stream, overwrite_output=True)
        logging.info(f"Extracted audio from {video_path} to {audio_path}")
        return audio_path
    except ffmpeg.Error as e:
        logging.error(f"FFmpeg error: {e}")
        raise
    except Exception as e:
        logging.error(f"Error extracting audio: {e}")
        raise
