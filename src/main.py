import os
from utils import read_data
from segmentation import generateSegments, generateSummaries, summarize_with_pegasus
from image_generation import generate_images
os.environ['CUDA_VISIBLE_DEVICES']='3'
import nltk
nltk.download('punkt')  # For tokenization
nltk.download('stopwords')
from nltk.tokenize import TextTilingTokenizer

data_folder = "../data/baseline2_try"
images_out_dir = "../generated_images/baseline2_try/"
df = read_data(data_folder)

df = generateSegments(df)

summarizer_model_id = "sshleifer/distilbart-xsum-12-6"

df1 = generateSummaries(df, summarizer_model_id)

df1.to_csv(images_out_dir+"/df_summary_distilbart.csv")


df2 = summarize_with_pegasus(df)
df2.to_csv(images_out_dir+"/df_summary_pegasus.csv")

# generate_images(df, images_out_dir)