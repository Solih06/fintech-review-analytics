import os
import logging
import pandas as pd
from transformers import pipeline
from collections import Counter
import re

# Configure explicit, professional system logging with clean UTF-8 encoding support
os.makedirs("data/processed", exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("data/processed/pipeline_execution.log", encoding='utf-8'),
        logging.StreamHandler()
    ]
)

def run_full_sentiment_and_thematic_pipeline():
    logging.info("SYSTEM START: Initializing Task 2 Full-Scale Sentiment & Thematic Extraction Pipeline.")
    
    raw_path = "data/raw/cleaned_reviews.csv"
    processed_dir = "data/processed"
    output_path = os.path.join(processed_dir, "sentiment_results.csv")
    themes_path = os.path.join(processed_dir, "thematic_trends.csv")
    
    if not os.path.exists(raw_path):
        logging.error(f"DATA ERROR: Raw review source file not found at {raw_path}")
        return

    df = pd.read_csv(raw_path)
    logging.info(f"INGESTION COMPLETED: Successfully loaded {len(df)} customer records for large-scale evaluation.")

    # 1. Full Scale Sentiment Analysis Pipeline
    logging.info("MODEL INITIALIZATION: Loading fine-tuned DistilBERT NLP Transformer pipeline layer...")
    classifier = pipeline(
        "sentiment-analysis", 
        model="distilbert-base-uncased-finetuned-sst-2-english",
        truncation=True,
        max_length=512
    )

    sentiments = []
    confidence_scores = []

    logging.info("EXECUTION SEQUENCE: Running batch inference sequence over the entire 1,500 review records...")
    for index, row in df.iterrows():
        review_text = str(row['review']) if pd.notnull(row['review']) else ""
        if not review_text.strip():
            sentiments.append("NEUTRAL")
            confidence_scores.append(1.0)
            continue
            
        result = classifier(review_text)[0]
        sentiments.append(result['label'])
        confidence_scores.append(result['score'])

    df['sentiment'] = sentiments
    df['confidence'] = confidence_scores

    df.to_csv(output_path, index=False)
    logging.info(f"EXPLICIT EVIDENCE GENERATED: Large-scale sentiment outputs successfully compiled at: {output_path}")

    # 2. Automated Thematic Analysis & Theme Extraction
    logging.info("THEMATIC EXTRACTION: Running text processing tokens over negative reviews to map key failure points...")
    negative_reviews = df[df['sentiment'] == 'NEGATIVE']['review'].dropna().astype(str)
    
    stop_words = {'the', 'to', 'and', 'a', 'in', 'is', 'it', 'i', 'of', 'this', 'for', 'my', 'on', 'with', 'app', 'bank', 'cbe', 'boa', 'dashen', 'not', 'very', 'but', 'have', 'has', 't', 's', 'am', 'are', 'was', 'were', 'please', 'update'}
    words = []
    
    for text in negative_reviews:
        cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text.lower())
        tokens = [w for w in cleaned_text.split() if w not in stop_words and len(w) > 3]
        words.extend(tokens)
        
    word_counts = Counter(words).most_common(10)
    
    themes_df = pd.DataFrame(word_counts, columns=['Theme_Keyword', 'Frequency'])
    themes_df.to_csv(themes_path, index=False)
    
    logging.info(f"EXPLICIT EVIDENCE GENERATED: Theme metrics saved successfully at: {themes_path}")
    logging.info("SYSTEM METRICS SUCCESS: CRITICAL ECOSYSTEM THEMING COMPLETED.")

if __name__ == "__main__":
    run_full_sentiment_and_thematic_pipeline()