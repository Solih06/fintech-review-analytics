# Fintech Review Analytics

An end-to-end data engineering and sentiment analysis pipeline designed to extract, clean, and analyze user reviews for major Ethiopian banking mobile applications (CBE, Bank of Abyssinia, and Dashen Bank). This project is developed as part of the Kifya training program.

## 📁 Project Structure

```text
fintech-review-analytics/
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows/
│       └── unittests.yml
├── .gitignore
├── requirements.txt
├── README.md
├── data/
│   ├── raw/                  # Raw scraped dataset (git-ignored)
│   └── processed/            # Processed datasets with sentiment labels & extracted themes
│       ├── sentiment_results.csv
│       └── thematic_trends.csv
├── notebooks/                # Notebooks and generated report visualizations
│   ├── __init__.py
│   ├── README.md
│   └── sentiment_distribution.png
├── src/
│   └── __init__.py
├── tests/
│   └── __init__.py
└── scripts/                  # Modular execution scripts
    ├── __init__.py
    ├── README.md
    ├── collect_data.py       # Task 1: Scraper & Preprocessing pipeline
    ├── analyze_sentiment.py  # Task 2: DistilBERT Sentiment & Thematic analysis
    └── generate_charts.py    # Visualizations generator
```

  ## 🛠️ Setup and Installation
   
1. ## Clone the repository:
   ```bash
   git clone [https://github.com/Solih06/fintech-review-analytics.git](https://github.com/Solih06/fintech-review-analytics.git)
   cd fintech-review-analytics
   
2. ## Set up Virtual Environment
   On Windows Powershell/CMD
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. ## Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
## 🚀 Execution Pipeline

The project pipeline is split into distinct, modular scripts executed in the following order:
## Step 1: Data Collection & Preprocessing

Extracts user reviews from Google Play Store for CBE, BOA, and Dashen apps, deduplicates data based on unique review IDs, standardizes schemas, and normalizes date ranges.
 ```bash
 python scripts/collect_data.py
  ```
## Step 2: Full-Scale Sentiment & Thematic Analytics (Task 2)

Leverages the Hugging Face Transformers pipeline loaded with a fine-tuned distilbert-base-uncased-finetuned-sst-2-english model to automatically append sentiment classifications and model confidence scores to the raw reviews across the entire 1,500 review dataset. It then tokenizes, filters stop-words, and calculates a frequency distribution to map key technical customer complaints.

  ```bash
  python scripts/analyze_sentiment.py
  ```
## Step 3: Visualization Generation

Aggregates the processed metrics and exports analytical plots reflecting cross-platform sentiment trends
  ```bash
  python scripts/generate_charts.py
  ```
## 💻 Core Technologies

    Language & Automation: Python 3.13

    Data Processing: Pandas, NumPy

    Machine Learning: Hugging Face (Transformers), PyTorch

    Data Visualization: Matplotlib, Seaborn


## 📊 Task 2 Performance & Large-Scale Evidence

The machine learning pipeline handles a deep learning sequence-classification pass over the full review dataset, saving comprehensive proof of execution directly inside the repository architecture.
1. ## Explicit Dataset Outputs

    Full Classified Output: Saved at data/processed/sentiment_results.csv (contains full text arrays mapped alongside model predictive labels and explicit prediction weights).

    Thematic Summary Metric Matrix: Saved at data/processed/thematic_trends.csv (contains the frequency tracking of critical failure points).

2. ## Automatic Thematic Analysis & Theme Extraction

By filtering down the critical negative reviews, the tracking pipeline automatically tokenizes text and computes distributions to isolate high-priority ecosystem pain points. The top extracted failure clusters include:

    Transactional Latency: High frequencies of payment timeouts and slow backend confirmations.

    Authentication Friction: Recurring user drop-offs linked to OTP (One-Time Password) generation delays.

    Account Sync Discrepancies: User interface reporting lag on real-time balance updates during peak traffic hours.

3. ## Sentiment Distribution across Fintech Apps

The comparative breakdown of user sentiment across the evaluated banking applications (CBE, BOA, and Dashen Bank) using 1,500 processed reviews:

## 📊 Visualizations
Sentiment Distribution across Fintech Apps. 
The following chart shows the comparative breakdown of user sentiment across the evaluated banking applications (CBE, BOA, and Dashen Bank) using 1,500 processed reviews:
![Sentiment Distribution](notebooks/sentiment_distribution.png)
