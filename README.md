# Premier League Analytics

A Python and SQLite application for exploring Premier League team and match data.

The project was built to develop practical skills in SQL, relational database design, Python, CSV data processing, and version control.

## Current Features

- View match results by season
- Look up team information
- Generate a league table from match results
- View season statistics for an individual team
- Rebuild the SQLite database from CSV source files

## Technologies

- Python
- SQLite
- SQL
- CSV
- Git and GitHub

## Project Structure

```text
premier-league-analytics/
├── data/
│   ├── matches.csv
│   ├── seasons.csv
│   └── teams.csv
├── database/
├── sql/
│   ├── create_tables.sql
│   └── queries.sql
├── src/
│   ├── database.py
│   ├── display.py
│   ├── main.py
│   └── setup_database.py
├── .gitignore
└── README.md
```

## Setup

### 1. Clone the repository

```powershell
git clone https://github.com/lucwiddowson/premier-league-analytics.git
cd premier-league-analytics
```

### 2. Create a virtual environment

```powershell
py -m venv .venv
```

### 3. Activate the virtual environment

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Build the database

```powershell
python src\setup_database.py
```

This creates the SQLite database and imports the team, season, and match data from the CSV files.

### 5. Run the application

```powershell
python src\main.py
```

## Database Design

The database currently contains three related tables.

### Teams

The `teams` table stores information about each football club, including:

- Team name
- City
- Stadium
- Year founded

### Seasons

The `seasons` table stores the available Premier League seasons.

### Matches

The `matches` table stores match results, including:

- Match date
- Season
- Home team
- Away team
- Home goals
- Away goals

The `matches` table connects to the `teams` and `seasons` tables using foreign keys.

## Application Options

When the application starts, the user can:

1. View matches by season
2. Look up a team
3. View a calculated league table
4. View team statistics for a selected season
5. Exit the application

## League Table Calculations

The application calculates league-table statistics directly from the match results.

The table includes:

- Matches played
- Wins
- Draws
- Losses
- Goals scored
- Goals conceded
- Goal difference
- Points

Teams receive:

- Three points for a win
- One point for a draw
- Zero points for a loss

The table is ordered by:

1. Points
2. Goal difference
3. Goals scored
4. Team name

## Data Import

The source data is stored in CSV files inside the `data` folder.

The `setup_database.py` script:

1. Deletes the existing local database
2. Creates the database tables
3. Imports teams
4. Imports seasons
5. Imports matches
6. Enables foreign-key checks

This allows the database to be rebuilt consistently from the source files.

## Future Improvements

- Import complete historical Premier League datasets
- Add team form analysis
- Add head-to-head comparisons
- Add home and away performance statistics
- Add charts and visualisations
- Build a graphical or web-based interface
- Add automated tests
- Improve input validation
- Support multiple complete seasons

## Purpose

This project is part of a programming portfolio and is being developed to build experience in:

- Writing SQL queries
- Designing relational databases
- Connecting Python to SQLite
- Processing CSV data
- Structuring a Python application
- Using Git and GitHub
- Building practical data-analysis tools
