import os
from utils import read_data
from segmentation import generateSegments
os.environ['CUDA_VISIBLE_DEVICES']='0'
import nltk
nltk.download('punkt')  # For tokenization
nltk.download('stopwords')
from nltk.tokenize import TextTilingTokenizer

data_folder = "./clean_dataset"
df = read_data(data_folder)

df = generateSegments(df)