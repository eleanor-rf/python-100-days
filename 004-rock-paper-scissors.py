import random
import sys

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices_list = [rock, paper, scissors]

for i in range (3):
    random_number = random.randint(0,2)
    computer_wins = 0
    player_wins = 0
    choice = input("What do you choose? Rock, paper, or scissors? ")

    if choice.lower() == "rock":
        print(f"{rock}\nComputer chose:\n{choices_list[random_number]}")
        if random_number == 0:
            print("It's a draw")
        elif random_number == 1:
            print("You lose")
            computer_wins+=1
        elif random_number == 2:
            print("You win!")
            player_wins+=1
        print(f"Current score - Computer: {computer_wins}, You: {player_wins}")

    elif choice.lower() == "scissors":
        print(f"{scissors}\nComputer chose:\n{choices_list[random_number]}")
        if random_number == 0:
            print("You lose")
            computer_wins+=1
        elif random_number == 1:
            print("You win!")
            player_wins+=1
        elif random_number == 2:
            print("It's a draw")
        print(f"Current score - Computer: {computer_wins}, You: {player_wins}")

    elif choice.lower() == "paper":
        print(f"{paper}\nComputer chose:\n{choices_list[random_number]}")
        if random_number == 0:
            print("You win!")
            player_wins+=1
        elif random_number == 1:
            print("It's a draw")
        elif random_number == 2:
            print("You lose!")
            computer_wins+=1
        print(f"Current score - Computer: {computer_wins}, You: {player_wins}")
    else:
        print("Didn't understand input, quitting")
        sys.exit()