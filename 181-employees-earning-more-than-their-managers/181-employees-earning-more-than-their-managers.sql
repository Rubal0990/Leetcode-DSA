# Write your MySQL query statement below
SELECT name AS Employee  FROM Employee AS T WHERE salary > (SELECT salary FROM Employee WHERE id=T.managerId)