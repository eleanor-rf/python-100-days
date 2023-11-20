print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice1 = input("You begin your adventure at a crossroads. Where do you want to go? Type 'left' or 'right'\n").lower()

if choice1 == "left":
    choice2 = input("You follow the left-hand path as it winds down to an estuary. It is currently too wide for you to walk across. You can swim or cross using the stepping stones which are rapidly becoming submerged. Type 'swim' or 'stones'\n").lower()
    if choice2 == "stones":
        choice3 = input("You struggle across the stepping stones. Mysterious hands reach out of the water and grasp at your ankles, but you slip free. You make it across, and beat through the forest to arrive at an imposing wall with three gates.\nWhich gate do you choose? Type 'red', 'blue' or 'yellow'.\n").lower()
        if choice3 == "yellow":
            print("You touch the handle of the yellow door and it feels warm. You push the door open to reveal the glittering hoard inside.\nYou win!")
        elif choice3 == "blue":
            print("You approach the blue door and an enormous beast throws the door straight off its hinges. You barely get the chance to get a look at the creature before its huge jaws bear down on you and it eats you alive.\nGame over.")
        elif choice3 == "red":
            print("You ease open the red door and step inside. A trapdoor opens beneath your feet and you are consumed in flames.\nGame over.")
        else:
            print("Your indecision costs you: you are exploded by a passing witch in a foul mood.\nGame over.")
    else:
        print("You attempt to swim across the river. A passing selkie offers you help. You take her slippery hand and she drowns you.\nGame over.")
else:
    print("You trip over a tree root and hit your head on a rock. When you wake up you have been dragged away by pixies.\nGame over.")

