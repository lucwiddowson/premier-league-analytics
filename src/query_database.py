import sqlite3
from pathlib import Path


DATABASE_PATH = Path("database/premier_league.db")


def get_matches():
    with sqlite3.connect(DATABASE_PATH) as connection:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                seasons.season_name,
                matches.match_date,
                home.team_name,
                away.team_name,
                matches.home_goals,
                matches.away_goals
            FROM matches
            JOIN seasons
                ON matches.season_id = seasons.season_id
            JOIN teams AS home
                ON matches.home_team_id = home.team_id
            JOIN teams AS away
                ON matches.away_team_id = away.team_id
            ORDER BY matches.match_date;
        """)

        return cursor.fetchall()


def display_matches(matches):
    for (
        season_name,
        match_date,
        home_team,
        away_team,
        home_goals,
        away_goals,
    ) in matches:
        print(
            f"{season_name} | {match_date} | "
            f"{home_team} {home_goals}-{away_goals} {away_team}"
        )


if __name__ == "__main__":
    matches = get_matches()
    display_matches(matches)