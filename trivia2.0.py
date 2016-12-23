#! python3

import json, requests, sys, random

topics = {'general': '9', 'movies': '11', 'tv': '14', 'science': '17', 'computers': '18',
          'math': '19', 'sports': '21', 'geography': '22', 'history': '23', 'animals': '27'}

print('Please Enter a Trivia Topic:')
for topic in topics.keys():
    print('\t' + topic)
category = input()
category = category.lower()

print('Select your difficulty (easy, medium, hard)')
difficulty = input()
difficulty = difficulty.lower()

# Download the JSON data from opentdb.com API
url = 'https://www.opentdb.com/api.php?amount=10&category=' + topics[category] + '&difficulty=' + difficulty + '&type=multiple'
response = requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable.
trivia = json.loads(response.text)
score = 0
for i in range(10):
    options = []
    correct_answer = trivia['results'][i]['correct_answer']
    correct_answer = correct_answer.replace('&quot;', '"', 4)
    options.append(correct_answer)
    for option in trivia['results'][i]['incorrect_answers']:
        option = option.replace('&quot;', '"', 4)
        option = option.replace('&#039;', '\'', 4)
        option = option.replace('&deg;', '°')
        options.append(option)
    
    random.shuffle(options)
    
    #print question w/choices
    question = trivia['results'][i]['question']
    question = question.replace('&quot;', '"', 4)
    question = question.replace('&deg;', '°')
    question = question.replace('&#039;', '\'', 4)
    print(str(i + 1) + ')' + question)
    print('\tA. ' + options[0])
    print('\tB. ' + options[1])
    print('\tC. ' + options[2])
    print('\tD. ' + options[3])

    #find correct answers index in options list
    if options.index(correct_answer) == 0:
        correct_letter = 'A'
    elif options.index(correct_answer) == 1:
        correct_letter = 'B'
    elif options.index(correct_answer) == 2:
        correct_letter = 'C'
    elif options.index(correct_answer) == 3:
        correct_letter = 'D'
    
    User_guess = input()
    User_guess = User_guess.upper()
    correct_guess = correct_letter + '. ' + correct_answer
    if User_guess in correct_guess:
        print('Correct!')
        score += 1
    else:
        print('Incorrect: ' + correct_answer)

def calculatePercent(per, whole):
    return (int(per) / int(whole)) * 100

print('Final Score: ' + str(score) + '/10')
percent = calculatePercent(score, 10)
print(str(percent) + '%')
if percent < 20.0:
    print('Ouch, go back to school!')
elif percent >= 20 and percent < 40.0:
    print('Hideous!!')
elif percent >= 40.0 and percent < 60.0:
    print('You need to try harder')
elif percent >= 60.0 and percent < 80.0:
    print('Ehh you did alright')
elif percent >= 80.0 and percent < 100.0:
    print('So close, yet so far')
elif percent == 100.0:
    print('You are a Trivia Master!')
