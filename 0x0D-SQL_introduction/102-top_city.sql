-- display top 3 by temperature
SELECT `city`, AVG(`value`) as avg_temp FROM temperatures
WHERE `month` = "July" OR `month` = "August"
GROUP BY `city`
ORDER BY avg_temp DESC
LIMIT 3;
