from preprocessing import handle_preprocessing
from input_detection import detect_input_type
from ai_story_generation import generate_ai_story
from audio_processing import process_audio_input
from sd_model_loader import pipe  # Import the Stable Diffusion pipeline
from generate_character_image import generate_character_images
from generate_character_image import generate_scene_image
from character_prompt_generator import extract_character_details
from character_extraction import extract_character_details  # Ensure this function exists
import os

# User input (can be text, audio, or AI-generated story)
user_input = input("Enter your story, audio file path, or AI story prompt: ")
input_type = detect_input_type(user_input)

# Process the input into a story format
story = handle_preprocessing(user_input)

if input_type == "audio":
    story = process_audio_input(user_input)  # Convert audio to text
elif input_type == "AI":
    story = generate_ai_story(user_input)

# Ensure story processing was successful
if story:
    print("\n✅ Generated/Processed Story:\n", story)

    # Extract character details from the story
    character_data = extract_character_details(story)  # ✅ Dictionary output

    if not isinstance(character_data, dict):
        print("\n❌ Error: Extracted character data is not in dictionary format!")
    else:
        print("\n✅ Extracted Character Data:", character_data)  # Debugging

        # Ensure valid character data before generating an image
        if "characters" in character_data and character_data["characters"]:
            # Set save path for the generated image
            save_directory = "generated_images"
            os.makedirs(save_directory, exist_ok=True)  # Ensure directory exists
            save_path = os.path.join(save_directory, "character_image.png")  # Set filename

            # ✅ Pass character list instead of dictionary
            reference_images = generate_character_images(character_data["characters"])
            
            # Generate a scene with multiple characters using reference images
            output_path = os.path.join(save_directory, "multi_character_image.png")
            generate_scene_image(character_data["characters"], reference_images, output_path)
        else:
            print("\n⚠️ No valid characters extracted!")
else:
    print("\n❌ Error processing input!")
