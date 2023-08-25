-- Calculate average temperatures for each city
SELECT city, avg(value) AS avg_temp
       FROM hbtn_0c_0
       GROUP BY city
       ORDER BY avg_tmp DESC;
