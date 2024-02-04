-- SQL file to insert 10 records into each table

-- insert records into 'vcrs'
INSERT INTO vcrs (model, availability) VALUES
('VCR-1001', 1),
('VCR-1002', 0),
('VCR-1003', 1),
('VCR-1004', 1),
('VCR-1005', 0),
('VCR-1006', 1),
('VCR-1007', 1),
('VCR-1008', 0),
('VCR-1009', 1),
('VCR-1010', 1);

-- insert records into 'customers'
INSERT INTO customers (name, contact_info) VALUES
('John Doe', 'john.doe@example.com'),
('Jane Smith', 'jane.smith@example.com'),
('Michael Johnson', 'michael.j@example.com'),
('Emily Davis', 'emily.davis@example.com'),
('Alex Martinez', 'alex.martinez@example.com'),
('Chris White', 'chris.white@example.com'),
('Jessica Thompson', 'jessica.t@example.com'),
('Sarah Clark', 'sarah.clark@example.com'),
('Brian Anderson', 'brian.anderson@example.com'),
('Olivia Thomas', 'olivia.thomas@example.com');

-- insert records into 'rentals'
INSERT INTO rentals (customer_id, vcr_id, rental_date, return_date) VALUES
(1, 2, '2023-01-10', '2023-01-20'),
(2, 3, '2023-02-15', '2023-02-25'),
(3, 4, '2023-03-10', '2023-03-20'),
(4, 5, '2023-04-05', '2023-04-15'),
(5, 1, '2023-05-01', '2023-05-11'),
(6, 2, '2023-06-07', '2023-06-17'),
(7, 3, '2023-07-04', '2023-07-14'),
(8, 4, '2023-08-09', '2023-08-19'),
(9, 5, '2023-09-02', '2023-09-12'),
(10, 1, '2023-10-10', '2023-10-20');
