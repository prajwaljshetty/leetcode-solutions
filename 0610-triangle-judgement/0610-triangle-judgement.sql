# Write your MySQL query statement below

-- SELECT T.* ,
-- CASE 
--     WHEN x + y > z 
--     AND  x + z > y 
--     AND  y + z > x
--     THEN "Yes"
--     ELSE "No"
-- END AS "triangle"
-- FROM Triangle T;

SELECT * , 
IF(x + y > z AND x + z > y AND y + z > x , "Yes" , "No") AS "triangle"
FROM Triangle;