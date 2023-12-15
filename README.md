# Story Visualization Generator

## Overview

This project introduces an innovative approach to generating visualizations from extensive text narratives. While existing models like Stable Diffusion and DALL-E-2 show promise in text-to-image synthesis, their word constraints limit their effectiveness for detailed content such as film scripts or educational materials. In response to this, we present an unsupervised, fully automatic pipeline that segments longer stories into meaningful scenes, then summarizes them to serve as prompts for image generation.

## Project Structure

The high-level project structure is organized as follows:

- **data:** Placeholder for project data.
  
  
- **generated_images:** Directory for storing generated images.
  
- **__pycache__:** Python cache files.

- **README.md:** Project documentation.

- **src:** Source code directory.

  - **eval.ipynb:** Jupyter notebook for evaluation.
    
  - **eval.py:** Python script for evaluation.

  - **generate_images.ipynb:** Jupyter notebook for generating images.
    
  - **image_generation.py:** Python script for image generation.

  - **main.ipynb:** Main Jupyter notebook for project execution.
    
  - **main.py:** Main Python script for project execution.

  - **prepare_baseline_data.ipynb:** Jupyter notebook for preparing baseline data.

  - **scrapper.ipynb:** Jupyter notebook for web scraping.

  - **scrapper_updated.ipynb:** Updated Jupyter notebook for web scraping.

  - **segmentation.py:** Python script for scene segmentation.

  - **story_cleaner.py:** Python script for cleaning story data.

  - **temp.ipynb:** Temporary Jupyter notebook.

  - **utils.py:** Utility functions for the project.
