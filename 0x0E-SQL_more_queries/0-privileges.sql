-- list all privileges for given users
SELECT * 
FROM mysql.user 
WHERE user IN ('user_0d_1', 'user_0d_2') 
  AND host = 'localhost';
