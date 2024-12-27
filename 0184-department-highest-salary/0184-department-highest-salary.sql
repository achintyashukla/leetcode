WITH cte AS (
    SELECT 
        name,
        salary,
        departmentId,
        RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) as rnk 
    FROM Employee
)

SELECT 
    d.name AS Department,
    c.name AS Employee,
    c.salary AS Salary 
FROM cte c 
LEFT JOIN Department d ON c.departmentId = d.id
WHERE c.rnk = 1;