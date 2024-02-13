-- average temprature by city 
SELECT `city`, AVG(`value`) as "avg_temp" FROM temperatures
ORDER BY AVG(`value`) DESC
