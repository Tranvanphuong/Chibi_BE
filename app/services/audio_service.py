import os
from pathlib import Path
from gtts import gTTS

# Define the base directory for audio files
AUDIO_DIR = Path("app/asset/speaking")

def generate_and_save_audio(word: str) -> str:
    """
    Generates an audio file for a given Japanese word using gTTS
    and saves it to the specified directory.
    If the file already exists, it returns the path to the existing file.

    Args:
        word (str): The Japanese word to convert to speech.

    Returns:
        str: The path to the generated or existing audio file.
    """
    # Ensure the audio directory exists
    AUDIO_DIR.mkdir(parents=True, exist_ok=True)

    file_name = f"{word}.mp3"
    file_path = AUDIO_DIR / file_name

    if file_path.exists():
        return str(file_path)
    
    try:
        tts = gTTS(text=word, lang='ja', slow=False)
        tts.save(file_path)
        return str(file_path)
    except Exception as e:
        print(f"Error generating audio for '{word}': {e}")
        raise
