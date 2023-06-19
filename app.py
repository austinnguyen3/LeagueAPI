from requests import HTTPError
from riotwatcher import LolWatcher

riotApiKey = "RGAPI-8f13e718-1564-4578-af5b-0402c844295c"
watcher = LolWatcher(riotApiKey)


def printSummonerInfo(platformRoutingValue, summonerName):
    if platformRoutingValue == "BR1" or "EUN1" or "JP1" or "KR" or "LA1" or "LA2" or "NA1" or "OC1" or "TR1" or "RU" \
            and summonerName != None:
        try:
            summoner = watcher.summoner.by_name(platformRoutingValue, summmonerName)
            print(summoner)
        except Exception as exception:
            print("Invalid Region or Summoner Name. Please Try Again.")


def printRankedStats(platformingRoutingValue, summonerName):
    if platformRoutingValue == "BR1" or "EUN1" or "JP1" or "KR" or "LA1" or "LA2" or "NA1" or "OC1" or "TR1" or "RU" \
            and summonerName != None:
        try:
            summoner = watcher.summoner.by_name(platformRoutingValue, summmonerName)
            ranked_stats = watcher.league.by_summoner(platformRoutingValue, summoner["id"])
            if not ranked_stats:
                print("No ranked stats from this season")
                exit()
            wins = float(ranked_stats[0]["wins"])
            losses = float(ranked_stats[0]["losses"])
            wins1 = float(ranked_stats[1]["wins"])
            losses1 = float(ranked_stats[1]["losses"])
            totalGames = wins + losses
            totalGames1 = wins1 + losses1
            winRate = str(round((((wins / totalGames) * 100)), 2))
            winRate1 = str(round((((wins1 / totalGames1) * 100)), 2))
            #print(ranked_stats)
            print("Queue Type: " + ranked_stats[0]["queueType"])
            print("Rank: " + ranked_stats[0]["tier"] + " " + ranked_stats[0]["rank"] + " " + str(
                ranked_stats[0]["leaguePoints"]) + " LP")
            print("Win Rate: " + winRate + chr(37))
            print("Queue Type: " + ranked_stats[1]["queueType"])
            print("Rank: " + ranked_stats[1]["tier"] + " " + ranked_stats[1]["rank"] + " " + str(
                ranked_stats[1]["leaguePoints"]) + " LP")
            print("Win Rate: " + winRate1 + chr(37))

        except Exception as exception:
            print("Invalid Region or Summoner Name. Please Try Again.")


platformRoutingValue = input("Enter Region: BR1\n"
                             "              EUN1\n"
                             "              EUW1\n"
                             "              JP1\n"
                             "              KR\n"
                             "              LA1\n"
                             "              LA2\n"
                             "              NA1\n"
                             "              OC1\n"
                             "              TR1\n"
                             "              RU\n")
summmonerName = input("Enter Summoner Name: ")
printSummonerInfo(platformRoutingValue, summmonerName)

printRankedStats(platformRoutingValue, summmonerName)
