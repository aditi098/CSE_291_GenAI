import nltk
import sys
import tqdm
from nltk.tokenize import TextTilingTokenizer
nltk.download('punkt') 
nltk.download('stopwords')

ttt = TextTilingTokenizer(w = 10, k=5)

def clean_segments(segments):
    clean_segment = []
    for segment in segments:
        if len(segment.strip())>10:
            clean_segments.append(segment)
    return clean_segment


def generateSegments(df, limit):
    print("Cleaning segments")
    works = 0
    not_works = 0
    all_segments = []

    for index, row in tqdm.tqdm(df.iterrows()):
    
        story = row["original_story"]
        try:
            segments = ttt.tokenize(story)
            all_segments.append(clean_segments(segments))
            works = works+1                
            
        except:
            not_works = not_works + 1
            all_segments.append([])
            
    print("segmentation works", works)
    print("segmentation doesn't work", not_works)
    
    df["segmented_story"] = all_segments
    return df



