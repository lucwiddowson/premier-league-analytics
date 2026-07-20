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


def get_team_by_name(team_name):
    with sqlite3.connect(DATABASE_PATH) as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                team_name,
                city,
                stadium,
                year_founded
            FROM teams
            WHERE LOWER(team_name) = LOWER(?);
            """,
            (team_name,),
        )

        return cursor.fetchone()


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


def display_team(team):
    if team is None:
        print("Team not found.")
        return

    team_name, city, stadium, year_founded = team

    print(f"Team: {team_name}")
    print(f"City: {city}")
    print(f"Stadium: {stadium}")
    print(f"Founded: {year_founded}")

def run_menu():
    print("Premier League Analytics")
    print("1. View all matches")
    print("2. Look up a team")

    choice = input("Choose an option: ")

    if choice == "1":
        matches = get_matches()
        display_matches(matches)

    elif choice == "2":
        team_name = input("Enter a team name: ")
        team = get_team_by_name(team_name)
        display_team(team)

    else:
        print("Invalid option.")

if __name__ == "__main__":
    run_menu()