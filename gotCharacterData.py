#! python3
# gotCharacterData.py - Prints Character data for GoT characters
# https://anapioficeandfire.com/

import json, requests, sys

# Compute name from command line arguments.
if len(sys.argv) < 2:
    print('Usage: gotCharacterData name')
    sys.exit()
name = ' '.join(sys.argv[1:])

# Download the JSON data 
url = 'http://www.anapioficeandfire.com/api/characters?name=' + name
response = requests.get(url)
response.raise_for_status()

characterData = json.loads(response.text)

#Name
print('\nCharacter name: ' + characterData[0]['name'])

#Gender
print('Gender: ' + characterData[0]['gender'])

#House Data
url2 = characterData[0]['allegiances'][0]
response2 = requests.get(url2)
response2.raise_for_status()
houseData = json.loads(response2.text)
print('\nAllegiance: ' + houseData['name'])
print('Sigil: ' + houseData['coatOfArms'])

#Birth/Death
print('\nBorn: ' + characterData[0]['born'])
if characterData[0]['died'] == '':
    print('Died: Still Alive')
else:
    print('Died: ' + characterData[0]['died'])

#Title Data
print('\nTitles: ')
print('-------')
counter1 = 0
for title in characterData[0]['titles']:
    print(characterData[0]['titles'][counter1])
    counter1 += 1

#Alias Data
print('\nAliases: ')
print('-------')
counter2 = 0
for alias in characterData[0]['aliases']:
    print(characterData[0]['aliases'][counter2])
    counter2 += 1

#TV Show
print('\nPlayed by: ' + characterData[0]['playedBy'][0])


