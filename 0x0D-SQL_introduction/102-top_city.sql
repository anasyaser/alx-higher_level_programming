-- Calculate average temperatures for each city during two months and filter top
SELECT city, avg(value) AS avg_temp
       FROM temperatures
       WHERE month = 7 OR month = 8
       GROUP BY city
       ORDER BY avg_temp DESC
       LIMIT 3;

