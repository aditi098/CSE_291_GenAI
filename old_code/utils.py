import os
import pandas as pd

#read dataset
def read_data(source_folder):
    # stories = {}
    dir_paths = []
    original_stories = []
    story_names = []
    df = pd.DataFrame()
    
    for dir_name in os.listdir(source_folder):
        if not dir_name.startswith(".DS_Store"):
            dir_path = os.path.join(source_folder, dir_name)
            dir_paths.append(dir_path)
            for dir_path in dir_paths:
                for story_name in os.listdir(dir_path):
                    if not story_name.startswith(".DS_Store"):
                        story_names.append(story_name)
                        story_path = os.path.join(dir_path, story_name)
                        file_path = story_path + "/story.txt"
                        with open(file_path, 'r') as file:
                            file_content = file.read()
                            file_content = file_content.encode().decode('unicode_escape')
                        original_stories.append(file_content)

    df["original_story"] = original_stories
    df["story_name"] = story_names 
    return df
