-- 1. Count complete review records per bank entity
SELECT b.bank_name, COUNT(r.review_id) as total_reviews
FROM reviews r
JOIN banks b ON r.bank_id = b.bank_id
GROUP BY b.bank_name;

-- 2. Compute aggregate rating distributions
SELECT b.bank_name, ROUND(AVG(r.rating), 2) as average_star_rating
FROM reviews r
JOIN banks b ON r.bank_id = b.bank_id
GROUP BY b.bank_name;

-- 3. Enforce data completeness audit (Look for accidental Null values)
SELECT COUNT(*) as records_missing_critical_text 
FROM reviews 
WHERE review_text IS NULL OR sentiment_label IS NULL;