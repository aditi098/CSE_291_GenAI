import os

# def restructure_fairytale_dataset(root_dir):
#     # The root directory of the dataset
#     dataset_dir = os.path.join(root_dir, 'dataset', 'fairy tale')

#     # Check if the dataset directory exists
#     if not os.path.exists(dataset_dir):
#         print(f"The directory '{dataset_dir}' does not exist.")
#         return

#     # Iterate over each fairytale directory
#     for fairytale in os.listdir(dataset_dir):
#         fairytale_dir = os.path.join(dataset_dir, fairytale)
        
#         # Check if it's a directory and contains the story.txt file
#         if os.path.isdir(fairytale_dir) and 'story.txt' in os.listdir(fairytale_dir):
#             # Build the new file path with concatenated name
#             new_file_name = fairytale.replace(' ', '_') + '.txt'
#             new_file_path = os.path.join(dataset_dir, new_file_name)

#             # Move and rename the story.txt to the new location
#             os.rename(os.path.join(fairytale_dir, 'story.txt'), new_file_path)

#             # Remove the now empty fairytale directory
#             os.rmdir(fairytale_dir)
#         else:
#             print(f"No story.txt found in '{fairytale_dir}'.")


# restructure_fairytale_dataset('/Users/samitkapadia/Desktop/Fall23/CSE_291_GenAI/')

def split_story_into_sentences(root_dir):
    # The root directory of the dataset
    dataset_dir = os.path.join(root_dir, 'dataset', 'fairy tale')

    # Check if the dataset directory exists
    if not os.path.exists(dataset_dir):
        print(f"The directory '{dataset_dir}' does not exist.")
        return

    # Iterate over each file in the fairytale directory
    for file in os.listdir(dataset_dir):
        file_path = os.path.join(dataset_dir, file)

        # Check if it's a text file
        if os.path.isfile(file_path) and file.endswith('.txt'):
            # Read the content of the file
            with open(file_path, 'r') as file:
                story_content = file.read()

            # Split the story into individual sentences
            sentences = story_content.split('. ')

            # Create a new file with sentences separated by a blank line
            with open(file_path, 'w') as file:
                for sentence in sentences:
                    file.write(sentence.strip() + '.\n\n')

split_story_into_sentences('/Users/samitkapadia/Desktop/Fall23/CSE_291_GenAI/')