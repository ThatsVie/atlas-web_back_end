-- List all Glam rock bands ranked by their longevity, handling split = 0 as active

SELECT band_name, 
       IFNULL(NULLIF(split, 0), YEAR(CURDATE())) - formed AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
