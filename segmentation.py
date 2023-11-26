import nltk
import sys
import tqdm
from nltk.tokenize import TextTilingTokenizer
nltk.download('punkt') 
nltk.download('stopwords')

ttt = TextTilingTokenizer(w = 10, k=5)

def generateSegments(df):
    works = 0
    not_works = 0
    print(len(df["original_story"]))
    for index, row in tqdm.tqdm(df.iterrows()):
        story = row["original_story"]
        try:
            segments = ttt.tokenize(story)
            works = works+1
        except:
            not_works = not_works + 1
    print("segmentation works", works)
    print("segmentation doesn't work", not_works)
    
    return df


# def getSummaries(stories):
    




