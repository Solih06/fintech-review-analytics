import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data array
results_path = os.path.join("data", "processed", "sentiment_results.csv")
df = pd.read_csv(results_path)

# Set visual style profiles
sns.set_theme(style="whitegrid")
os.makedirs("notebooks", exist_ok=True)

# Plot 1: Rating Densities Across Banks (Boxplot/Violin to check stars)
plt.figure(figsize=(10, 5))
sns.boxplot(x='bank', y='rating', data=df, palette="Set2")
plt.title("User Rating Star Distributions by Bank Application")
plt.xlabel("Bank Entity")
plt.ylabel("Star Rating (1-5)")
plt.savefig("notebooks/rating_distribution_boxplot.png", dpi=300, bbox_inches='tight')
plt.close()

# Plot 2: Sentiment Aggregations across Star Ratings
plt.figure(figsize=(10, 5))
sns.barplot(x='rating', y='sentiment_score', hue='bank', data=df, errorbar=None, palette="viridis")
plt.title("Model Sentiment Confidence Scores Across Star Buckets")
plt.xlabel("Star Rating Provided by User")
plt.ylabel("Average Sentiment Confidence Weight")
plt.savefig("notebooks/sentiment_vs_rating.png", dpi=300, bbox_inches='tight')
plt.close()

print("Task 4 advanced executive visualization plots saved cleanly to the notebooks/ directory.")