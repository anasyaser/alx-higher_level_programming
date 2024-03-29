-- Calculate the max temp for each state
SELECT state, max(value) AS max_temp
       FROM temperatures
       GROUP BY state
       ORDER BY state;
