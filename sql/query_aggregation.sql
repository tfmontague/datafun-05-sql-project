-- SQL file to use aggregation functions including COUNT, AVG, SUM

-- Aggregation query on the 'rentals' table, to gain insights about the rental periods of VCRs. Calculate the total number of rentals, the average rental period, and the sum of all rental periods in days.
SELECT 
    COUNT(id) AS total_rentals,
    AVG(julianday(return_date) - julianday(rental_date)) AS avg_rental_duration,
    SUM(julianday(return_date) - julianday(rental_date)) AS total_rental_days
FROM rentals;
