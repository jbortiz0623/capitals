# an array of state dictionaries
states = [
{
    "name": "Alabama",
    "capital": "Montgomery"
}, {
    "name": "Alaska",
    "capital": "Juneau"
}, {
    "name": "Arizona",
    "capital": "Phoenix"
}, {
    "name": "Arkansas",
    "capital": "Little Rock"
}, {
    "name": "California",
    "capital": "Sacramento"
}, {
    "name": "Colorado",
    "capital": "Denver"
}, {
    "name": "Connecticut",
    "capital": "Hartford"
}, {
    "name": "Delaware",
    "capital": "Dover"
}, {
    "name": "Florida",
    "capital": "Tallahassee"
}, {
    "name": "Georgia",
    "capital": "Atlanta"
}, {
    "name": "Hawaii",
    "capital": "Honolulu"
}, {
    "name": "Idaho",
    "capital": "Boise"
}, {
    "name": "Illinois",
    "capital": "Springfield"
}, {
    "name": "Indiana",
    "capital": "Indianapolis"
}, {
    "name": "Iowa",
    "capital": "Des Moines"
}, {
    "name": "Kansas",
    "capital": "Topeka"
}, {
    "name": "Kentucky",
    "capital": "Frankfort"
}, {
    "name": "Louisiana",
    "capital": "Baton Rouge"
}, {
    "name": "Maine",
    "capital": "Augusta"
}, {
    "name": "Maryland",
    "capital": "Annapolis"
}, {
    "name": "Massachusetts",
    "capital": "Boston"
}, {
    "name": "Michigan",
    "capital": "Lansing"
}, {
    "name": "Minnesota",
    "capital": "St. Paul"
}, {
    "name": "Mississippi",
    "capital": "Jackson"
}, {
    "name": "Missouri",
    "capital": "Jefferson City"
}, {
    "name": "Montana",
    "capital": "Helena"
}, {
    "name": "Nebraska",
    "capital": "Lincoln"
}, {
    "name": "Nevada",
    "capital": "Carson City"
}, {
    "name": "New Hampshire",
    "capital": "Concord"
}, {
    "name": "New Jersey",
    "capital": "Trenton"
}, {
    "name": "New Mexico",
    "capital": "Santa Fe"
}, {
    "name": "New York",
    "capital": "Albany"
}, {
    "name": "North Carolina",
    "capital": "Raleigh"
}, {
    "name": "North Dakota",
    "capital": "Bismarck"
}, {
    "name": "Ohio",
    "capital": "Columbus"
}, {
    "name": "Oklahoma",
    "capital": "Oklahoma City"
}, {
    "name": "Oregon",
    "capital": "Salem"
}, {
    "name": "Pennsylvania",
    "capital": "Harrisburg"
}, {
    "name": "Rhode Island",
    "capital": "Providence"
}, {
    "name": "South Carolina",
    "capital": "Columbia"
}, {
    "name": "South Dakota",
    "capital": "Pierre"
}, {
    "name": "Tennessee",
    "capital": "Nashville"
}, {
    "name": "Texas",
    "capital": "Austin"
}, {
    "name": "Utah",
    "capital": "Salt Lake City"
}, {
    "name": "Vermont",
    "capital": "Montpelier"
}, {
    "name": "Virginia",
    "capital": "Richmond"
}, {
    "name": "Washington",
    "capital": "Olympia"
}, {
    "name": "West Virginia",
    "capital": "Charleston"
}, {
    "name": "Wisconsin",
    "capital": "Madison"
}, {
    "name": "Wyoming",
    "capital": "Cheyenne"
}]

# `print`
# - `input`
# - `for loop`
# - `sorted`
# - `random.shuffle()`
import random

random.shuffle(states)

print('Welcome to the State Game!')
print('If it is correct you will get a point. If you are incorrect you will lose a point.')

def state_game ():
    wrong = 0
    correct = 0
    score = correct - wrong

    i = 0

    while i < len(states):
        print ('What is the capital of '+ states[i]['name'] )
        answer = input()
        if answer == states[i]['capital']:
            correct = correct + 1
            print("Awesome you got it!")
            print(f"You have answered {correct} correctly and {wrong} incorrectly.")
            print(f"Total scrore is {score}")
        else:
            wrong = wrong + 1
            print("Aww boo. That is incorrect.")
            print(f"You have answered {correct} correctly and {wrong} incorrectly.")
            print(f"Total scrore is {score}")
        i = i + 1

    print(f'What a game! Your final score was {score} out of 50')


state_game()

print('Would you like to play again?')
answer = input()

if answer == 'y' or 'yes' :
    state_game()
else:
    print('Goodbye')
    exit()```


   while i < len(states):
        print ('What is the capital of '+ states[i]['name'] )
        answer = input()
        if answer == states[i]['capital']:
            correct = correct + 1
            score = correct - wrong
            print("Awesome you got it!")
            print(f"You have answered {correct} correctly and {wrong} incorrectly.")
            print(f"Total scrore is {score}")

        else:
            wrong = wrong + 1
            score = correct - wrong
            print("Aww boo. That is incorrect.")
            print(f"You have answered {correct} correctly and {wrong} incorrectly.")
            print(f"Total scrore is {score}")
        i = i + 1
