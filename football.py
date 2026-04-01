from dotenv import load_dotenv
import os
import requests
import datetime

load_dotenv()

API_KEY = os.getenv("FOOTBALL_API_KEY")
BASE_URL = "https://api.football-data.org/v4"
headers = {"X-Auth-Token" : API_KEY}

def get_standings(league_code):
    response = requests.get(f'{BASE_URL}/competitions/{league_code}/standings', headers=headers)
    data = response.json()

    standings = data["standings"][0]["table"]

    print(f'\n{'Pos':<5}{'Team':<30}{'P':<5}{'W':<5}{'D':<5}{'L':<5}{'GF':<5}{'GA':<5}{'GD':<5}{'Pts':<5}')
    print('-' * 74)

    for team in standings:
        print(f'{team["position"]:<5}{team["team"]["name"]:<30}{team["playedGames"]:<5}{team["won"]:<5}{team["draw"]:<5}{team["lost"]:<5}{team["goalsFor"]:<5}{team["goalsAgainst"]:<5}{team["goalDifference"]:<5}{team["points"]:<5}')

def get_todays_matches():
    todays_date = datetime.date.today()
    todays_date = todays_date.strftime("%Y-%m-%d")

    response = requests.get(f'{BASE_URL}/matches?date={todays_date}', headers = headers)
    data = response.json()

    matches = data["matches"]

    for match in matches:
        print(f'{match['competition']['name']} | {match['homeTeam']['name']} vs {match['awayTeam']['name']} - {match['utcDate'][11:16]}')


get_todays_matches()
# get_standings("PL")