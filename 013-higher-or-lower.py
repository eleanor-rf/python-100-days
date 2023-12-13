import random
import os

data = {
    'Adders-tongue fern': 1260,
    'Atlas blue butterfly': 448,
    'Black mulberry': 308,
    'Field horsetail': 216,
    'African baobab tree': 168,
    'Walking catfish': 104,
    'Aquatic rat': 92,
    'Prawn': 86,
    'Bloody geranium': 84,
    'Pigeon': 80,
    'Tropical pitcher plant': 78,
    'Polar bear': 74,
    'White-tailed deer': 70,
    'Elk': 68,
    'Chinchilla': 64,
    'Mule': 63,
    'Donkey': 62,
    'American bison': 60,
    'Elephant': 58,
    'Strawberry': 56,
    'Sheep': 54,
    'Platypus': 52,
    'Pineapple': 50,
    '❤Eurasian beaver❤': 48, # beavers are legitimately my favourite animal
    'Human': 46,
    'Moon jellyfish': 44,
    'Rat': 42,
    'Peanut': 40,
    'Cat': 38,
    'Earthworm': 36,
    'Sunflower': 34,
    'Baker\'s yeast': 32,
    'Giraffe': 30,
    'Axolotl': 28,
    'European beech': 24,
    'Runner bean': 22,
    'Maize': 20,
    'Passionfruit': 18,
    'Garlic': 16,
    'Tasmanian devil': 14,
    'Spinach': 12,
    'Arabidopsis thaliana (thale cress)': 10,
    'Fruit fly': 8,
    'Indiac muntjac': 6,
    'Jack jumper ant': 1
}

keys = list(data.keys())
random.shuffle(keys) # access key-value pairs in dictionary in random order
score = 0
winning = True
currentKey = 0
i = 1

print("Welcome to the higher or lower game.")

while (winning):
    print(f"Compare A: {keys[currentKey]}\nAgainst B: {keys[currentKey+i]}")
    guess = input("Who has the highest chromosome number? Type A or B: ").lower()
    while guess not in ['a','b']:
        guess = input("Didn't understand input. Type A or B: ")
    os.system('cls' if os.name == 'nt' else 'clear')

    if guess == 'a':
        if data[keys[currentKey]] > data[keys[currentKey+i]]:
            score+=1
            print(f"You're right! Current score = {score}")
            i+=1
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            winning = False
    elif guess == 'b':
        if data[keys[currentKey+i]] > data[keys[currentKey]]:
            score+=1
            print(f"You're right! Current score = {score}")
            currentKey += 1
            i += 1
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            winning = False