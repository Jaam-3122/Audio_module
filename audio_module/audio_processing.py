import speech_recognition as sr
from text_processing import process_text_input

def process_audio_input(audio_path):
    """
    Converts audio to text using speech recognition and processes it as text input.
    :param audio_path: Path to audio file.
    :return: Embeddings and transcribed text.
    """
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f"Transcribed Audio to Text: {text}")
        return process_text_input(text), text  
    except Exception as e:
        print(f"Error in audio processing: {e}")
        return None, None
