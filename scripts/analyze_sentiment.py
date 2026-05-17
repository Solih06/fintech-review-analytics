import os
import pandas as pd
from transformers import pipeline
from collections import Counter
import re

def run_full_sentiment_and_thematic_pipeline():
    print("🚀 Starting Task 2: Advanced Sentiment & Thematic Analysis...")
    
    raw_path = "data/raw/cleaned_reviews.csv"
    processed_dir = "data/processed"
    output_path = os.path.join(processed_dir, "sentiment_results.csv")
    themes_path = os.path.join(processed_dir, "thematic_trends.csv")
    
    if not os.path.exists(raw_path):
        print(f"❌ Error: Raw data file not found at {raw_path}")
        return

    # Load full dataset
    df = pd.read_csv(raw_path)
    print(f"📋 Loaded {len(df)} records for processing.")

    # 1. Full Scale Sentiment Analysis
    print("🧠 Initializing DistilBERT Transformer pipeline...")
    classifier = pipeline(
        "sentiment-analysis", 
        model="distilbert-base-uncased-finetuned-sst-2-english",
        truncation=True,
        max_length=512
    )

    sentiments = []
    confidence_scores = []

    print("⚡ Analyzing full review dataset (this may take a moment)...")
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

    # Ensure processed directory exists and save large scale evidence
    os.makedirs(processed_dir, exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"💾 Saved explicit large-scale sentiment output evidence to: {output_path}")

    # 2. Thematic Analysis / Theme Extraction
    print("🔍 Extracting prominent complaint themes from negative reviews...")
    negative_reviews = df[df['sentiment'] == 'NEGATIVE']['review'].dropna().astype(str)
    
    # Simple tokenization & cleaning loop to isolate infrastructure themes
    stop_words = {'the', 'to', 'and', 'a', 'in', 'is', 'it', 'i', 'of', 'this', 'for', 'my', 'on', 'with', 'app', 'bank', 'cbe', 'boa', 'dashen', 'not', 'very', 'but', 'have', 'has', 't', 's', 'am', 'are', 'was', 'were'}
    words = []
    
    for text in negative_reviews:
        cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text.lower())
        tokens = [w for w in cleaned_text.split() if w not in stop_words and len(w) > 2]
        words.extend(tokens)
        
    word_counts = Counter(words).most_common(10)
    
    # Save themes to a tracked dataframe
    themes_df = pd.DataFrame(word_counts, columns=['Theme/Keyword', 'Frequency'])
    themes_df.to_csv(themes_path, index=False)
    print(f"💾 Saved theme extraction metrics to: {themes_path}")
    print("\n👑 Top Extracted Issues/Themes:")
    print(themes_df)

if __name__ == "__main__":
    run_full_sentiment_and_thematic_pipeline()