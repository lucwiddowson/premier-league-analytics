import csv
from datetime import datetime
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_DATA_PATH = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "premier_league_2025_26.csv"
)

OUTPUT_PATH = PROJECT_ROOT / "data" / "matches.csv"

SEASON_ID = 1


TEAM_IDS = {
    "Arsenal": 1,
    "Aston Villa": 2,
    "Bournemouth": 3,
    "Brentford": 4,
    "Brighton": 5,
    "Burnley": 6,
    "Chelsea": 7,
    "Crystal Palace": 8,
    "Everton": 9,
    "Fulham": 10,
    "Leeds": 11,
    "Liverpool": 12,
    "Man City": 13,
    "Man United": 14,
    "Newcastle": 15,
    "Nott'm Forest": 16,
    "Sunderland": 17,
    "Tottenham": 18,
    "West Ham": 19,
    "Wolves": 20,
}


def convert_date(date_text):
    parsed_date = datetime.strptime(date_text, "%d/%m/%Y")
    return parsed_date.strftime("%Y-%m-%d")


def get_team_id(team_name):
    try:
        return TEAM_IDS[team_name]
    except KeyError as error:
        raise ValueError(
            f"Unknown team name in source data: {team_name}"
        ) from error


def read_raw_matches():
    matches = []

    with RAW_DATA_PATH.open(
        "r",
        encoding="utf-8-sig",
        newline="",
    ) as csv_file:
        reader = csv.DictReader(csv_file)

        for match_id, row in enumerate(reader, start=1):
            match = {
                "match_id": match_id,
                "season_id": SEASON_ID,
                "match_date": convert_date(row["Date"]),
                "home_team_id": get_team_id(row["HomeTeam"]),
                "away_team_id": get_team_id(row["AwayTeam"]),
                "home_goals": int(row["FTHG"]),
                "away_goals": int(row["FTAG"]),
            }

            matches.append(match)

    return matches


def write_matches(matches):
    column_names = [
        "match_id",
        "season_id",
        "match_date",
        "home_team_id",
        "away_team_id",
        "home_goals",
        "away_goals",
    ]

    with OUTPUT_PATH.open(
        "w",
        encoding="utf-8",
        newline="",
    ) as csv_file:
        writer = csv.DictWriter(
            csv_file,
            fieldnames=column_names,
        )

        writer.writeheader()
        writer.writerows(matches)


def main():
    matches = read_raw_matches()
    write_matches(matches)

    print(f"Processed {len(matches)} matches.")
    print(f"Created: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()