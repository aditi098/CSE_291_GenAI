import os
from utils import read_data
from segmentation import generateSegments, generateSummaries
from image_generation import generate_images
os.environ['CUDA_VISIBLE_DEVICES']='2'
import nltk
nltk.download('punkt')  # For tokenization
nltk.download('stopwords')
from nltk.tokenize import TextTilingTokenizer

data_folder = "../data/clean_dataset"
images_out_dir = "../generated_images/baseline2_full/"
df = read_data(data_folder)

df = generateSegments(df)

summarizer_model_id = "sshleifer/distilbart-xsum-12-6"

df = generateSummaries(df, summarizer_model_id)

df.to_csv(images_out_dir+"/df_summary.csv")

generate_images(df, images_out_dir)