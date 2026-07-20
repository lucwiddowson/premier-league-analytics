import sqlite3
from pathlib import Path


database_path = Path("database/premier_league.db")

connection = sqlite3.connect(database_path)
cursor = connection.cursor()

cursor.execute("""
    SELECT
        team_name,
        city,
        stadium,
        year_founded
    FROM teams
    ORDER BY team_name;
""")

teams = cursor.fetchall()

for team_name, city, stadium, year_founded in teams:
    print(
        f"{team_name} | {city} | "
        f"{stadium} | Founded {year_founded}"
    )

connection.close()