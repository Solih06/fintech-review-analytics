-- 1. Create Lookup Table for Banks
CREATE TABLE IF NOT EXISTS banks (
    bank_id INT PRIMARY KEY,
    bank_name VARCHAR(100) NOT NULL,
    app_name VARCHAR(100) NOT NULL
);

-- 2. Create Core Table for Scraped & Processed Reviews
CREATE TABLE IF NOT EXISTS reviews (
    review_id VARCHAR(100) PRIMARY KEY,
    bank_id INT NOT NULL,
    review_text TEXT,
    rating INT CHECK (rating >= 1 AND rating <= 5),
    review_date TIMESTAMP NOT NULL,
    sentiment_label VARCHAR(20),
    sentiment_score NUMERIC(5, 4),
    identified_theme VARCHAR(100),
    source VARCHAR(50) DEFAULT 'Google Play',
    FOREIGN KEY (bank_id) REFERENCES banks(bank_id) ON DELETE CASCADE
);