from riotwatcher import TftWatcher, ApiError
import pandas as pd

# global variables
api_key = "RGAPI-a328498c-aad4-40ff-85e5-b9d8726ae1e4"
watcher = TftWatcher(api_key)
region = "na1"
match_region = "americas"

league = watcher.league.challenger(region)
for entry in league["entries"]:
    name = entry["summonerName"]
    if ("C9 k3soju" in name):
        print(name)
        player = watcher.summoner.by_name(region, name)
        match_id = watcher.match.by_puuid(match_region, player["puuid"], 1)
        print("Latest match info:")
        print(watcher.match.by_id(match_region, match_id[0]))
