import nltk
import sys
import tqdm
import os
from nltk.tokenize import TextTilingTokenizer
nltk.download('punkt') 
nltk.download('stopwords')
from transformers import pipeline
from collections import defaultdict
os.environ['CUDA_LAUNCH_BLOCKING'] = "1"
ttt = TextTilingTokenizer(w = 10, k=5)
device = "cuda:2"
from transformers import PegasusForConditionalGeneration, PegasusTokenizer

def clean_segments(segments):
    clean_segment = []
    for segment in segments:
        if len(segment.strip())>10:
            clean_segment.append(segment.strip())
    return clean_segment


def generateSegments(df):
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


def generateSummaries(df, summarizer_model_id):
    
    pipe = pipeline("summarization", model=summarizer_model_id, max_length=20)
    all_summaries = []
    
    for index, row in tqdm.tqdm(df.iterrows()):
        summaries = []
        segments = row["segmented_story"]
        for segment in segments:
            try:
                summary = pipe(segment)
                summaries.append(summary[0]['summary_text'])
            except Exception as e:
                print(f"An error occurred with model {summarizer_model_id}: {e}")
                summaries.append(segment)
                #append original segment in case of error
        all_summaries.append(summaries)
        
    df["summarized_story"] = all_summaries
    return df


def summarize_with_pegasus(df, model_name="google/pegasus-xsum", max_length=60, min_length=20):
    
    all_summaries = []
    tokenizer = PegasusTokenizer.from_pretrained(model_name)
    model = PegasusForConditionalGeneration.from_pretrained(model_name)
    for index, row in tqdm.tqdm(df.iterrows()):
        summaries = []
        segments = row["segmented_story"]
        for segment in segments:
            try:
                tokens = tokenizer(segment, truncation=True, padding="longest", return_tensors="pt")
                summary_ids = model.generate(tokens["input_ids"], max_length=max_length, min_length=min_length, length_penalty=2.0, num_beams=4, early_stopping=True)
                summaries.append(tokenizer.decode(summary_ids[0], skip_special_tokens=True))
            except Exception as e:
                print(f"An error occurred with model {model_name}: {e}")
                summaries.append(segment)
                #append original segment in case of error
        all_summaries.append(summaries)
        
    df["summarized_story"] = all_summaries
    return df
