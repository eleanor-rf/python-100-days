import random
art = __import__('007-hangman-art')
import os

stages = art.stages

with open("007-hangman-wordlist.txt") as f:
    word_list = f.read().splitlines()

chosen_word = random.choice(word_list)
print(chosen_word) # test word choice

display = []
for letter in chosen_word:
    display.append('_')

game_over = False

lives = 6

guessed_letters = []

print(art.logo)

while not game_over:
    guess = (input("Guess a letter: ")).lower()
    if guess in guessed_letters:
        print(f"You already guessed {guess}! Pick another letter.")
    
    else:
        guessed_letters.append(guess)
        os.system('cls' if os.name == 'nt' else 'clear')

        for i in range (len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
        if guess not in chosen_word:
            lives -= 1
            print(stages[lives])
            print(f"{guess} is not in the word. You have {lives} lives remaining.")
    
        print(f"\n{' '.join(display)}\n\nGuessed letters: {' '.join(guessed_letters)}\n")

        if lives == 0:
            game_over = True
            print(f"You lose. The word was {chosen_word}.")
    
        if '_' not in display:
            game_over = True
            print("You win!")
