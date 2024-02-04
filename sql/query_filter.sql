-- SQL file to filter data

-- Filter Rentals Longer Than 10 Days
SELECT *
FROM rentals
WHERE julianday(return_date) - julianday(rental_date) > 10;

