import torch
import clip
from PIL import Image
from torchvision.transforms import Compose, Resize, CenterCrop, ToTensor, Normalize
import os
import pandas as pd

# Load CLIP model
device = "cuda:2" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

# Function to calculate CLIP score
def calculate_clip_score(text, image_path):
    print("Running calculate_clip_score")
    image = preprocess(Image.open(image_path)).unsqueeze(0).to(device)
    text = clip.tokenize([text]).to(device)

    with torch.no_grad():
        image_features = model.encode_image(image)
        text_features = model.encode_text(text)

        similarity = torch.cosine_similarity(text_features, image_features).cpu().numpy()

        # Get the logits representing the similarity score
        # logits = model(image_features, text_features).logits_per_image

    # return logits.item()
        # print(similarity)
        return similarity[0]

# Function to process a story
def process_story(df, story_name, image_folder):
    print("Running process_story")
    story_df = df[df['topic'].str.contains(story_name)]
    # story_df = df[story_filter]
    scores = []

    for _, row in story_df.iterrows():
        # print("Checking in: ",row['text'])
        segment_no = row['topic'].split('_')[-1]

        print("segment_no: ", segment_no)
        image_filename1 = f"stories_{story_name}_{segment_no}.jpg"
        image_filename2 = f"stories_{story_name}_segment_{segment_no}.jpg"
        image_path1 = os.path.join(image_folder, image_filename1)
        image_path2 = os.path.join(image_folder, image_filename2)
        # print(image_path)
        if os.path.exists(image_path1):
          image_path = image_path1
        elif os.path.exists(image_path2):
          image_path = image_path2

        if os.path.exists(image_path):
            # print(image_path)
            # print(row['summary'])
            score = calculate_clip_score(row['summary'], image_path)
            scores.append(score)

    return sum(scores) / len(scores) if scores else 0
    # return scores
    
    
# Directory containing images
image_folder = "../evaluation_data/baseline1/experiment_samit_fairy_tale_segmented"

# Stories to process
stories = ['cat and mouse in partnership', 'clever hans_segment', 'domestic servants']
# stories = ['cat and mouse in partnership', 'domestic servants']

# DataFrame containing text, topic, summary
df_images = pd.read_csv('/content/df_images.csv')
df_images.head()

average_scores = {story: process_story(df_images, story, image_folder) for story in stories}