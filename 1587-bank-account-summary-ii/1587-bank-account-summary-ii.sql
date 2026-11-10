# Write your MySQL query statement below

SELECT name , sum(amount) as balance FROM Users U 
JOIN Transactions T 
ON U.account = T.account
GROUP BY T.account
HAVING sum(amount) > 10000;