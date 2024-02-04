-- SQL query to use GROUP BY clause

-- Query to Count Rentals per VCR
SELECT vcr_id, COUNT(*) AS rental_count
FROM rentals
GROUP BY vcr_id
ORDER BY rental_count DESC;
