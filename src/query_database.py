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


def get_seasons():
    with sqlite3.connect(DATABASE_PATH) as connection:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                season_id,
                season_name
            FROM seasons
            ORDER BY season_name DESC;
        """)

        return cursor.fetchall()


def get_league_table(season_id):
    with sqlite3.connect(DATABASE_PATH) as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
            WITH team_results AS (
                SELECT
                    matches.home_team_id AS team_id,
                    1 AS played,
                    CASE
                        WHEN matches.home_goals > matches.away_goals THEN 1
                        ELSE 0
                    END AS won,
                    CASE
                        WHEN matches.home_goals = matches.away_goals THEN 1
                        ELSE 0
                    END AS drawn,
                    CASE
                        WHEN matches.home_goals < matches.away_goals THEN 1
                        ELSE 0
                    END AS lost,
                    matches.home_goals AS goals_for,
                    matches.away_goals AS goals_against,
                    CASE
                        WHEN matches.home_goals > matches.away_goals THEN 3
                        WHEN matches.home_goals = matches.away_goals THEN 1
                        ELSE 0
                    END AS points
                FROM matches
                WHERE matches.season_id = ?

                UNION ALL

                SELECT
                    matches.away_team_id AS team_id,
                    1 AS played,
                    CASE
                        WHEN matches.away_goals > matches.home_goals THEN 1
                        ELSE 0
                    END AS won,
                    CASE
                        WHEN matches.away_goals = matches.home_goals THEN 1
                        ELSE 0
                    END AS drawn,
                    CASE
                        WHEN matches.away_goals < matches.home_goals THEN 1
                        ELSE 0
                    END AS lost,
                    matches.away_goals AS goals_for,
                    matches.home_goals AS goals_against,
                    CASE
                        WHEN matches.away_goals > matches.home_goals THEN 3
                        WHEN matches.away_goals = matches.home_goals THEN 1
                        ELSE 0
                    END AS points
                FROM matches
                WHERE matches.season_id = ?
            )

            SELECT
                teams.team_name,
                COALESCE(SUM(team_results.played), 0) AS played,
                COALESCE(SUM(team_results.won), 0) AS won,
                COALESCE(SUM(team_results.drawn), 0) AS drawn,
                COALESCE(SUM(team_results.lost), 0) AS lost,
                COALESCE(SUM(team_results.goals_for), 0) AS goals_for,
                COALESCE(SUM(team_results.goals_against), 0) AS goals_against,
                COALESCE(SUM(team_results.points), 0) AS points
            FROM teams
            LEFT JOIN team_results
                ON teams.team_id = team_results.team_id
            GROUP BY
                teams.team_id,
                teams.team_name
            ORDER BY
                points DESC,
                goals_for - goals_against DESC,
                goals_for DESC,
                teams.team_name ASC;
            """,
            (season_id, season_id),
        )

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


def display_team(team):
    if team is None:
        print("Team not found.")
        return

    team_name, city, stadium, year_founded = team

    print(f"Team: {team_name}")
    print(f"City: {city}")
    print(f"Stadium: {stadium}")
    print(f"Founded: {year_founded}")


def display_seasons(seasons):
    for season_id, season_name in seasons:
        print(f"{season_id}. {season_name}")


def display_league_table(table):
    print(
        f"{'Team':<20}"
        f"{'P':>3}"
        f"{'W':>3}"
        f"{'D':>3}"
        f"{'L':>3}"
        f"{'GF':>4}"
        f"{'GA':>4}"
        f"{'GD':>4}"
        f"{'Pts':>5}"
    )

    for (
        team_name,
        played,
        won,
        drawn,
        lost,
        goals_for,
        goals_against,
        points,
    ) in table:
        goal_difference = goals_for - goals_against

        print(
            f"{team_name:<20}"
            f"{played:>3}"
            f"{won:>3}"
            f"{drawn:>3}"
            f"{lost:>3}"
            f"{goals_for:>4}"
            f"{goals_against:>4}"
            f"{goal_difference:>4}"
            f"{points:>5}"
        )


def run_menu():
    while True:
        print("\nPremier League Analytics")
        print("1. View all matches")
        print("2. Look up a team")
        print("3. View league table")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            matches = get_matches()
            display_matches(matches)

        elif choice == "2":
            team_name = input("Enter a team name: ")
            team = get_team_by_name(team_name)
            display_team(team)

        elif choice == "3":
            seasons = get_seasons()

            if not seasons:
                print("No seasons found.")
                continue

            display_seasons(seasons)
            season_id = input("Choose a season ID: ")

            if not season_id.isdigit():
                print("Invalid season ID.")
                continue

            table = get_league_table(int(season_id))
            display_league_table(table)

        elif choice == "4":
            print("Goodbye.")
            break

        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    run_menu()