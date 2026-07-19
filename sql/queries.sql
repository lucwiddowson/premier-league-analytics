SELECT team_name, stadium, year_founded
FROM teams;

SELECT team_name, stadium
FROM teams
WHERE city = 'London';

SELECT team_name, year_founded
FROM teams
ORDER BY year_founded ASC;

SELECT team_name, city, stadium
FROM teams
ORDER BY team_name ASC;

SELECT team_name, year_founded
FROM teams
WHERE year_founded < 1900;

SELECT team_name, city
FROM teams
WHERE city != 'London';

SELECT team_name, year_founded
FROM teams
WHERE year_founded BETWEEN 1880 AND 1900;

SELECT team_name, city, year_founded
FROM teams
WHERE city = 'London'
AND year_founded < 1900;

SELECT team_name, stadium
FROM teams
WHERE year_founded >= 1892 
ORDER BY year_founded DESC;

SELECT team_name, city
FROM teams
WHERE city = 'London'
OR city = 'Manchester';

SELECT team_name, city
FROM teams
WHERE city IN ('London', 'Manchester');

SELECT team_name
FROM teams
WHERE team_name LIKE '%United%';

SELECT team_name, stadium
FROM teams
WHERE stadium LIKE '%Stadium%';