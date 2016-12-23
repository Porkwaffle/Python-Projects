#! python3
# quickWeather.py - Prints the current weather for a location from the command line.

import json, requests, sys

# Compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()
title = ' '.join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API
url ='http://www.omdbapi.com/?t=' + title + '&y=&plot=short&r=json'
response = requests.get(url)
response.raise_for_status()

movieData = json.loads(response.text)

print('Movie title: ' + movieData['Title'])
print('Year: ' + movieData['Year'])
print('Language: ' + movieData['Language'])
print('Runtime: ' + movieData['Runtime'])
print('IMDB Rating: ' + movieData['imdbRating'])
print('Actors: ' + movieData['Actors'])
