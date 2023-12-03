import os
import multiprocessing
from story_cleaner import clean_story  # Import the function from the separate file

base_path = "./dataset/short story"
output_base_path = "./clean_dataset/short_story"
folders = os.listdir(base_path)

def process_folder(folder):
    clean_story(folder, base_path, output_base_path)

if __name__ == '__main__':
    # Using multiprocessing
    pool = multiprocessing.Pool()
    pool.map(process_folder, folders)
    pool.close()
    pool.join()