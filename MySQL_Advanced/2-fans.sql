-- This query will rank the countries based on the total number of fans, ordered in descending order.

SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
