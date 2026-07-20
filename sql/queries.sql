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

SELECT COUNT(*) AS total_teams
FROM teams;

SELECT MIN(year_founded) AS oldest_founding_year
FROM teams;

SELECT MAX(year_founded) AS newest_founding_year
FROM teams;

SELECT AVG(year_founded) AS average_founding_year
FROM teams;

SELECT city, COUNT(*) AS number_of_teams
FROM teams
GROUP BY city
ORDER BY number_of_teams DESC;

SELECT COUNT(*) AS historic_teams
FROM teams
WHERE year_founded < 1900;

SELECT
    matches.match_date,
    home.team_name AS home_team,
    away.team_name AS away_team,
    matches.home_goals,
    matches.away_goals
FROM matches
JOIN teams AS home
    ON matches.home_team_id = home.team_id
JOIN teams AS away
    ON matches.away_team_id = away.team_id;

SELECT
    matches.match_date,
    home.team_name AS home_team,
    away.team_name AS away_team,
    matches.home_goals || '-' || matches.away_goals AS score
FROM matches
JOIN teams AS home
    ON matches.home_team_id = home.team_id
JOIN teams AS away
    ON matches.away_team_id = away.team_id;