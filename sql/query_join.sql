-- SQL query to use INNER JOIN operation

-- Query to Combine Rentals and Customers Information
SELECT rentals.id AS rental_id, 
       customers.name AS customer_name, 
       rentals.rental_date, 
       rentals.return_date
FROM rentals
INNER JOIN customers ON rentals.customer_id = customers.id
ORDER BY rentals.rental_date;
