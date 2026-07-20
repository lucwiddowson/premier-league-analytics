import sqlite3
from pathlib import Path


DATABASE_PATH = Path("database/premier_league.db")


def get_matches(season_id):
    with sqlite3.connect(DATABASE_PATH) as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
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
            WHERE matches.season_id = ?
            ORDER BY matches.match_date;
            """,
            (season_id,),
        )

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


def get_team_season_stats(team_name, season_id):
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
            WHERE LOWER(teams.team_name) = LOWER(?)
            GROUP BY
                teams.team_id,
                teams.team_name;
            """,
            (season_id, season_id, team_name),
        )

        return cursor.fetchone()


def get_seasons():
    with sqlite3.connect(DATABASE_PATH) as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                season_id,
                season_name
            FROM seasons
            ORDER BY season_name DESC;
            """
        )

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