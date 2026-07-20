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