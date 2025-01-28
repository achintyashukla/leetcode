# Write your MySQL query statement below
SELECT class
FROM Courses
WHERE class IS NOT NULL
GROUP BY class
HAVING COUNT(*) >= 5;