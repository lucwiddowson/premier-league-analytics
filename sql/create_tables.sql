-- Premier League Analytics Database
-- This file creates the database tables.

CREATE TABLE teams (
    team_id INTEGER PRIMARY KEY,
    team_name TEXT,
    city TEXT,
    stadium TEXT,
    year_founded INTEGER
);

CREATE TABLE matches (
    match_id INTEGER PRIMARY KEY,
    match_date TEXT,
    home_team_id INTEGER,
    away_team_id INTEGER,
    home_goals INTEGER,
    away_goals INTEGER
);