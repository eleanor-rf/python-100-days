import random
import sys

print("Welcome to the number guessing game!\nI'm thinking of a number between 1 and 100.")
correct_answer = random.randint(1,100)
# print(f"### DEBUG: the correct answer is {correct_answer}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

def game(difficulty):
    if difficulty == 'easy':
        attempts_remaining = 10
    elif difficulty == 'hard':
        attempts_remaining = 5
    while attempts_remaining > 0:
        print(f"You have {attempts_remaining} attempts remaining.")
        while True:
            try:
                guess = int(input("Guess a number: "))
                break
            except ValueError:
                guess = input("Didn't understand input. Type a number: ").lower()
        if guess == correct_answer:
            print(f"You got it! The answer was {correct_answer}.")
            sys.exit()
        elif guess < correct_answer:
            print("Too low. Guess again.")
            attempts_remaining -= 1
        elif guess > correct_answer:
            print("Too high. Guess again.")
            attempts_remaining -= 1
    print(f"You lose! The correct answer was {correct_answer}.")
    sys.exit()

while difficulty not in ['easy', 'hard']:
    difficulty = input("Didn't understand input. Type 'easy' or 'hard': ").lower()

game(difficulty)