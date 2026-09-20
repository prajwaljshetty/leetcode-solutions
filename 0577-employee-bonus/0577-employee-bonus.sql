# Write your MySQL query statement below

SELECT E.name as name , B.bonus as bonus FROM Employee E LEFT JOIN Bonus B ON E.empId = B.empId where B.bonus is NULL or B.bonus < 1000;
