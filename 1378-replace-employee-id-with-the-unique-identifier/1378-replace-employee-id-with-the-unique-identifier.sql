# Write your MySQL query statement below
SELECT unique_id , name
FROM EmployeeUNI AS e
RIGHT JOIN Employees AS u
ON e.id = u.id;