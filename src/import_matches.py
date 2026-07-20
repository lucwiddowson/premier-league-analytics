import csv
import sqlite3
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATABASE_PATH = PROJECT_ROOT / "database" / "premier_league.db"
CSV_PATH = PROJECT_ROOT / "data" / "matches.csv"


def read_matches_from_csv():
    matches = []

    with CSV_PATH.open("r", encoding="utf-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            match = (
                int(row["match_id"]),
                int(row["season_id"]),
                row["match_date"],
                int(row["home_team_id"]),
                int(row["away_team_id"]),
                int(row["home_goals"]),
                int(row["away_goals"]),
            )

            matches.append(match)

    return matches


def insert_matches(matches):
    with sqlite3.connect(DATABASE_PATH) as connection:
        cursor = connection.cursor()

        cursor.executemany(
            """
            INSERT OR REPLACE INTO matches (
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


def main():
    matches = read_matches_from_csv()
    insert_matches(matches)

    print(f"Imported {len(matches)} matches.")


if __name__ == "__main__":
    main()