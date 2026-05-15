import pandas as pd
from transformers import pipeline
import os

def run_sentiment_analysis():
    input_path = 'data/raw/cleaned_reviews.csv'
    output_dir = 'data/processed'
    output_path = os.path.join(output_dir, 'sentiment_results.csv')

    if not os.path.exists(input_path):
        print(f"[X] Error: {input_path} not found. Run collect_data.py first.")
        return

    print("Loading dataset...")
    df = pd.read_csv(input_path)

    print("Initializing DistilBERT Sentiment Pipeline...")
    # This specific model is fine-tuned for sentiment and fits the challenge requirements
    classifier = pipeline(
        "sentiment-analysis", 
        model="distilbert-base-uncased-finetuned-sst-2-english"
    )

    print(f"Analyzing {len(df)} reviews. Please wait...")
    
    # Process reviews
    # truncation=True ensures we don't crash on long reviews
    results = classifier(df['review'].tolist(), truncation=True)
    
    # Extract results
    df['sentiment'] = [res['label'] for res in results]
    df['confidence'] = [res['score'] for res in results]

    # Save the processed data
    os.makedirs(output_dir, exist_ok=True)
    df.to_csv(output_path, index=False)
    
    print("\n" + "="*40)
    print("TASK 2: SENTIMENT ANALYSIS COMPLETE")
    print(f"File saved to: {output_path}")
    print("\nQuick Summary:")
    print(df['sentiment'].value_counts())
    print("="*40)

if __name__ == "__main__":
    run_sentiment_analysis()