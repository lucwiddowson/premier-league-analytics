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

    print(f"\nTeam: {team_name}")
    print(f"City: {city}")
    print(f"Stadium: {stadium}")
    print(f"Founded: {year_founded}")


def display_team_season_stats(stats):
    if stats is None:
        print("Team not found.")
        return

    (
        team_name,
        played,
        won,
        drawn,
        lost,
        goals_for,
        goals_against,
        points,
    ) = stats

    goal_difference = goals_for - goals_against

    print(f"\nTeam: {team_name}")
    print(f"Played: {played}")
    print(f"Wins: {won}")
    print(f"Draws: {drawn}")
    print(f"Losses: {lost}")
    print(f"Goals for: {goals_for}")
    print(f"Goals against: {goals_against}")
    print(f"Goal difference: {goal_difference}")
    print(f"Points: {points}")


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