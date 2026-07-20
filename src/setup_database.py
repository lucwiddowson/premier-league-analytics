import csv
import sqlite3
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATABASE_PATH = PROJECT_ROOT / "database" / "premier_league.db"
CREATE_TABLES_PATH = PROJECT_ROOT / "sql" / "create_tables.sql"

TEAMS_CSV_PATH = PROJECT_ROOT / "data" / "teams.csv"
SEASONS_CSV_PATH = PROJECT_ROOT / "data" / "seasons.csv"
MATCHES_CSV_PATH = PROJECT_ROOT / "data" / "matches.csv"


def create_database():
    if DATABASE_PATH.exists():
        DATABASE_PATH.unlink()

    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)

    create_tables_sql = CREATE_TABLES_PATH.read_text(encoding="utf-8")

    with sqlite3.connect(DATABASE_PATH) as connection:
        connection.executescript(create_tables_sql)

    print("Created database tables.")


def read_teams():
    teams = []

    with TEAMS_CSV_PATH.open("r", encoding="utf-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            teams.append(
                (
                    int(row["team_id"]),
                    row["team_name"],
                    row["city"],
                    row["stadium"],
                    int(row["year_founded"]),
                )
            )

    return teams


def read_seasons():
    seasons = []

    with SEASONS_CSV_PATH.open("r", encoding="utf-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            seasons.append(
                (
                    int(row["season_id"]),
                    row["season_name"],
                )
            )

    return seasons


def read_matches():
    matches = []

    with MATCHES_CSV_PATH.open("r", encoding="utf-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            matches.append(
                (
                    int(row["match_id"]),
                    int(row["season_id"]),
                    row["match_date"],
                    int(row["home_team_id"]),
                    int(row["away_team_id"]),
                    int(row["home_goals"]),
                    int(row["away_goals"]),
                )
            )

    return matches


def insert_teams(connection, teams):
    connection.executemany(
        """
        INSERT INTO teams (
            team_id,
            team_name,
            city,
            stadium,
            year_founded
        )
        VALUES (?, ?, ?, ?, ?);
        """,
        teams,
    )


def insert_seasons(connection, seasons):
    connection.executemany(
        """
        INSERT INTO seasons (
            season_id,
            season_name
        )
        VALUES (?, ?);
        """,
        seasons,
    )


def insert_matches(connection, matches):
    connection.executemany(
        """
        INSERT INTO matches (
            match_id,
            season_id,
            match_date,
            home_team_id,
            away_team_id,
            home_goals,
            away_goals
        )
        VALUES (?, ?, ?, ?, ?, ?, ?);
        """,
        matches,
    )


def import_data():
    teams = read_teams()
    seasons = read_seasons()
    matches = read_matches()

    with sqlite3.connect(DATABASE_PATH) as connection:
        connection.execute("PRAGMA foreign_keys = ON;")

        insert_teams(connection, teams)
        insert_seasons(connection, seasons)
        insert_matches(connection, matches)

    print(f"Imported {len(teams)} teams.")
    print(f"Imported {len(seasons)} seasons.")
    print(f"Imported {len(matches)} matches.")


def main():
    create_database()
    import_data()

    print("Database setup complete.")


if __name__ == "__main__":
    main()