# Write your MySQL query statement below
WITH temp as (SELECT num , count(*) FROM MyNumbers GROUP BY num HAVING COUNT(*) = 1)
SELECT max(num) as num FROM temp;