import requests
import json

nameOfShow = input('Hello! Enter the name of the show: \n')

omdbBaseUrl = 'http://www.omdbapi.com/?'

omdb_my_atts = {'r': 'json',  't': nameOfShow}

omdb_resp = requests.get(omdbBaseUrl, params = omdb_my_atts)

IMDBdata = omdb_resp.json()

imdbID = IMDBdata["imdbID"]

# tv maze search for next episode

tvMazeBaseUrl = 'http://api.tvmaze.com/lookup/shows?'

tvMaze_my_atts = {'imdb': imdbID}

tvMaze_resp = requests.get(tvMazeBaseUrl, params = tvMaze_my_atts)

tvMazedata = tvMaze_resp.json()

nextEpisodeURL = tvMazedata['_links']['nextepisode']['href']
nextEpisodeCountry = tvMazedata['network']['country']['name']
nextEpisodeURL_resp = requests.get(nextEpisodeURL)

nextEpisodeData = nextEpisodeURL_resp.json()

print("\n")

nextEpisodeNumber = str(nextEpisodeData['number'])
nextEpisodeSeason = str(nextEpisodeData['season'])
nextEpisodeDate = nextEpisodeData['airdate']
nextEpisodeTime = nextEpisodeData['airtime']
nextEpisodeName = nextEpisodeData['name']


print("The next episode [Episode " + nextEpisodeNumber + " - " + nextEpisodeName + "] of season " + nextEpisodeSeason + " of " + nameOfShow + " will premiere on " + nextEpisodeDate + " at " + nextEpisodeTime + " in " + nextEpisodeCountry)
