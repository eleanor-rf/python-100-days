import random
import sys

start = input("Do you want to play a game of blackjack? Type 'y' or 'n': ").lower()
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

if start == 'y':
    lost = False
    your_hand = [cards[random.randint(0,12)], cards[random.randint(0,12)]]
    running_total = your_hand[0] + your_hand[1]
    computer_hand = [cards[random.randint(0,12)], cards[random.randint(0,12)]]
    computer_total = computer_hand[0] + computer_hand[1]
    print(f"Your hand: {your_hand}. Current total = {running_total}")
    print(f"Computer's first card: {computer_hand[0]}")
    draw_again = input("Do you want to draw again? 'y' or 'n': ")
    while draw_again not in ['y', 'n']:
        print("Didn't understand input. Please enter 'y' or 'n'.")
        draw_again = input("Do you want to draw again? 'y' or 'n': ").lower()

    while draw_again == 'y' and not lost:
        your_hand.append(cards[random.randint(0,12)])
        running_total += your_hand[-1]
        print(f"Your cards: {your_hand}. Current total = {running_total}")
        print(f"Computer's first card: {computer_hand[0]}")

        if running_total > 21:
            lost = True
            print(f"Your final hand: {your_hand}, final score = {running_total}")
            print(f"Computer's final hand: {computer_hand}, final score = {computer_total}")
            print("You lose! You went over 21.")
            sys.exit()
        
        draw_again = input("Do you want to draw again? 'y' or 'n': ")
    
    print(f"Your final hand: {your_hand}, your final total: {running_total}")
    print(f"Computer's hand: {computer_hand}, computer's final total: {computer_total}")
    if running_total > computer_total:
        print("You win!")
    elif running_total == computer_total:
        print("It's a draw!")
    elif running_total < computer_total:
        print("You lose!")
