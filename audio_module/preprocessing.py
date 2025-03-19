from input_detection import detect_input_type
from ai_story_generation import generate_ai_story
from audio_processing import process_audio_input
def handle_preprocessing(input_data):
    """
    Handles preprocessing for text, audio, or AI-generated story inputs.
    Returns only the processed story, as embeddings are not needed.
    """
    input_type = detect_input_type(input_data)
    story = ""

    if input_type == "text":
        story = input_data
    elif input_type == "audio":
        _, story = process_audio_input(input_data)  # Extracts text from audio
    elif input_type == "ai_story":
        story = generate_ai_story(input_data)
    else:
        print("Invalid input type detected!")
        return None

    return story  # Only returning the processed story
