-- join tables
INSERT INTO cities (state_id, name) VALUES (1, 'San Jose')
INSERT INTO cities (state_id, name) VALUES (2, 'Page')
INSERT INTO cities (state_id, name) VALUES (3, 'Paris')
INSERT INTO cities (state_id, name) VALUES (3, 'Houston')
INSERT INTO cities (state_id, name) VALUES (3, 'Dallas')
-- SELECT id, name
-- FROM cities
-- WHERE state_id = (
--     SELECT id 
--     FROM states 
--     WHERE name = 'California'
-- )
-- ORDER BY id ASC;
