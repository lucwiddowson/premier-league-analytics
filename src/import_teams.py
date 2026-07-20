import csv
import sqlite3
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATABASE_PATH = PROJECT_ROOT / "database" / "premier_league.db"
CSV_PATH = PROJECT_ROOT / "data" / "teams.csv"


def read_teams_from_csv():
    teams = []

    with CSV_PATH.open("r", encoding="utf-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            team = (
                int(row["team_id"]),
                row["team_name"],
                row["city"],
                row["stadium"],
                int(row["year_founded"]),
            )

            teams.append(team)

    return teams


def insert_teams(teams):
    with sqlite3.connect(DATABASE_PATH) as connection:
        cursor = connection.cursor()

        cursor.executemany(
            """
            INSERT OR REPLACE INTO teams (
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


def main():
    teams = read_teams_from_csv()
    insert_teams(teams)

    print(f"Imported {len(teams)} teams.")


if __name__ == "__main__":
    main()