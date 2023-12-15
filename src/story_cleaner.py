import os
import re

def clean_story(folder, base_path, output_base_path):
    if folder.startswith('.DS_Store'):
        return

    print(f"Processing folder: {folder}")
    
    file_path = os.path.join(base_path, folder, 'story.txt')
    new_folder = os.path.join(output_base_path, folder)
    new_file_path = os.path.join(new_folder, 'story.txt')

    with open(file_path, 'r') as file:
        story_text = file.read().replace('\n', ' ').replace('"', "'")

    # Regular expression operations
    regex_featured = re.compile(r'.*? was featured as .*')
    regex_numbers = re.compile(r'\s*\d+\.?\d*\s*$')

    # List of fixed markers
    fixed_markers = ["Add A", "Read the next short story", "Return to the", "\n\n\t\n\n\t\n\n\t\n\n\t", "\n\n\t"]
    marker_positions = [story_text.find(marker) for marker in fixed_markers if marker in story_text]
    marker_positions.append(regex_featured.search(story_text).start() if regex_featured.search(story_text) else -1)

    # Filter out -1 and find minimum position
    valid_positions = [pos for pos in marker_positions if pos != -1]
    if valid_positions:
        story_text = story_text[:min(valid_positions)]

    # Remove numbers at the end of the text
    story_text = regex_numbers.sub('', story_text)

    # Create the output directory and write the cleaned text
    os.makedirs(new_folder, exist_ok=True)
    with open(new_file_path, 'w') as new_file:
        new_file.write(story_text)

    print(f"Finished processing: {folder}")
