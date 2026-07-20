from database import (
    get_league_table,
    get_matches,
    get_seasons,
    get_team_by_name,
    get_team_season_stats,
)
from display import (
    display_league_table,
    display_matches,
    display_seasons,
    display_team,
    display_team_season_stats,
)


def choose_season():
    seasons = get_seasons()

    if not seasons:
        print("No seasons found.")
        return None

    display_seasons(seasons)
    season_id = input("Choose a season ID: ")

    if not season_id.isdigit():
        print("Invalid season ID.")
        return None

    return int(season_id)


def run_menu():
    while True:
        print("\nPremier League Analytics")
        print("1. View matches by season")
        print("2. Look up a team")
        print("3. View league table")
        print("4. View team season statistics")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            season_id = choose_season()

            if season_id is None:
                continue

            matches = get_matches(season_id)

            if not matches:
                print("No matches found for that season.")
                continue

            display_matches(matches)

        elif choice == "2":
            team_name = input("Enter a team name: ")
            team = get_team_by_name(team_name)
            display_team(team)

        elif choice == "3":
            season_id = choose_season()

            if season_id is None:
                continue

            table = get_league_table(season_id)
            display_league_table(table)

        elif choice == "4":
            season_id = choose_season()

            if season_id is None:
                continue

            team_name = input("Enter a team name: ")
            stats = get_team_season_stats(team_name, season_id)
            display_team_season_stats(stats)

        elif choice == "5":
            print("Goodbye.")
            break

        else:
            print("Invalid option. Please choose 1, 2, 3, 4, or 5.")


if __name__ == "__main__":
    run_menu()