# Write your MySQL query statement below
SELECT e1.name
FROM Employee AS e1
INNER JOIN Employee AS e2
ON e2.managerID = e1.id
GROUP BY e1.id , e1.name
HAVING COUNT(e1.id) >= 5