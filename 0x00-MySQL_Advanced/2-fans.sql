-- SQL script to rank country origins of bands oredered by number of fans
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands 
GROUP BY origin
ORDER BY nb_fans DESC;
