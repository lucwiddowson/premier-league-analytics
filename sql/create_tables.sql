-- Premier League Analytics Database
-- This file creates the database tables.

CREATE TABLE teams (
    team_id INTEGER PRIMARY KEY,
    team_name TEXT,
    city TEXT,
    stadium TEXT,
    year_founded INTEGER
);

CREATE TABLE seasons (
    season_id INTEGER PRIMARY KEY,
    season_name TEXT
);

CREATE TABLE matches (
    match_id INTEGER PRIMARY KEY,
    season_id INTEGER,
    match_date TEXT,
    home_team_id INTEGER,
    away_team_id INTEGER,
    home_goals INTEGER,
    away_goals INTEGER,
    FOREIGN KEY (season_id) REFERENCES seasons(season_id),
    FOREIGN KEY (home_team_id) REFERENCES teams(team_id),
    FOREIGN KEY (away_team_id) REFERENCES teams(team_id)
);