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