--  list all cities contained in the database hbtn_0d_usa
SELECT cities.id, cities.name AS name, states.name AS name
FROM hbtn_0d_usa.cities
INNER JOIN hbtn_0d_usa.states ON cities.state_id = states.id
ORDER BY cities.id ASC;
