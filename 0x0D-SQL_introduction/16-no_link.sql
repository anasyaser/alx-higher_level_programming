-- Don't Display null names
SELECT score, name FROM second_table
where name IS NOT NULL
ORDER BY score DESC;