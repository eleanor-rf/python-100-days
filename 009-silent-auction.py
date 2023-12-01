import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
more_bidders = "yes"
bidders = {}

while more_bidders == "yes":
    name = input("What is your name? ")
    bid = int(input("How much would you like to bid? £"))
    bidders[name] = bid
    more_bidders = input("Are there any more bidders? Type yes or no: ")
    os.system('cls' if os.name == 'nt' else 'clear')

max = 0
max_bidder = ""
for key,value in bidders.items():
    if value > max:
        max = value
        max_bidder = key

print(f"The winner is {max_bidder}. The maximum bid was {max}.")