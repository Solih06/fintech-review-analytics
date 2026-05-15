import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def create_plots():
    input_path = 'data/processed/sentiment_results.csv'
    if not os.path.exists(input_path):
        print(f"[X] Error: Run analyze_sentiment.py first.")
        return

    df = pd.read_csv(input_path)
    
    # Aggregate data for the stacked chart
    pivot_df = df.groupby(['bank', 'sentiment']).size().unstack(fill_value=0)
    
    # Setup styling
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(10, 6))
    
    # Plot stacked bar
    pivot_df.plot(kind='bar', stacked=True, color=['#e74c3c', '#2ecc71'], alpha=0.85, ax=plt.gca())
    
    plt.title('Fintech App Customer Sentiment Distribution by Bank', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Financial Institution', fontsize=12, labelpad=10)
    plt.ylabel('Number of Reviews', fontsize=12, labelpad=10)
    plt.xticks(rotation=0)
    plt.legend(title='Sentiment', frameon=True)
    
    # Save chart to notebooks/ or report directory
    os.makedirs('notebooks', exist_ok=True)
    chart_path = 'notebooks/sentiment_distribution.png'
    plt.tight_layout()
    plt.savefig(chart_path, dpi=300)
    plt.close()
    
    print("\n" + "="*40)
    print("VISUALIZATION GENERATED")
    print(f"Chart saved to: {chart_path}")
    print("\nUse these exact figures the report text:")
    print(pivot_df)
    print("="*40)

if __name__ == "__main__":
    create_plots()