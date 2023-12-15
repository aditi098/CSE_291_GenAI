# Story Visualization Generator

## Overview

This project introduces an innovative approach to generating visualizations from extensive text narratives. While existing models like Stable Diffusion and DALL-E-2 show promise in text-to-image synthesis, their word constraints limit their effectiveness for detailed content such as film scripts or educational materials. In response to this, we present an unsupervised, fully automatic pipeline that segments longer stories into meaningful scenes, then summarizes them to serve as prompts for image generation.

## Project Structure

The high-level project structure is organized as follows:

- **data:** Placeholder for project data.
  
- **generated_images:** Directory for storing generated images.

- **src:** Source code directory.

  - **eval.ipynb:** code for clip score and image coherency evaluation.

  - **generate_test_images.ipynb:** Jupyter notebook for generating some test images.
    
  - **image_generation.py:** Python script for image generation using text2img diffusion models.
    
  - **main.py:** Main Python script for project execution.

  - **prepare_baseline_data.ipynb:** Jupyter notebook for preparing baseline data.

  - **scrapper.ipynb:** code for scraping dataset from the source website(americanliterature.com).

  - **segmentation.py:** Python script for segmentation of stories.

  - **story_cleaner.py:** Python script for preprocessing text in stories.

  - **utils.py:** Utility functions for the project.
 
To run the project

1. Clone the github repo 
```
   git clone <repository_url>
```
2. Set up requirements
   ```
   pip install -r requirements.txt
    ```
4. Run
   ```
   python src/main.py
   ```

