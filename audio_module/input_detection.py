import os

def detect_input_type(input_data):
    """
    Automatically detects whether the input is text, audio, or an AI story prompt.
    
    :param input_data: User-provided input (text or file path).
    :return: Detected input type ('text', 'audio', 'ai_story').
    """

    if isinstance(input_data, str):
        # Check if input is a valid file path and an audio file
        if os.path.isfile(input_data) and input_data.lower().endswith(('.wav', '.mp3', '.flac', '.ogg')):
            return "audio"
        # If input is short, assume it's a prompt for AI story generation
        elif len(input_data.split()) < 10:
            return "ai_story"
        else:
            return "text"
    else:
        raise ValueError("Unsupported input type detected.")

# Example Test Cases
if __name__ == "__main__":
    print(detect_input_type("Hello, create a story!"))  # ai_story
    print(detect_input_type("This is a long paragraph that should be classified as text."))  # text
    print(detect_input_type("audio_sample.wav"))  # If the file exists, it'll return 'audio', else an error
