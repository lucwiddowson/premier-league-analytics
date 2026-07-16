-- Premier League Analytics Database
-- This file creates the database tables.

CREATE TABLE teams (
    team_id INTEGER PRIMARY KEY,
    team_name TEXT,
    city TEXT,
    stadium TEXT,
    year_founded INTEGER
);