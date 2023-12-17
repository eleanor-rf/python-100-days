resource_values = {
    'water': 1200,
    'milk': 700,
    'coffee': 120,
    'money': 0.0
}

requirements = {
    'latte': {
        'water': 150,
        'milk': 200,
        'coffee': 16,
        'money': 2.2,
    },
    'espresso': {
        'water': 80,
        'milk': 0,
        'coffee': 16,
        'money': 1.2,
    },
    'cappuccino': {
        'water': 150,
        'milk': 180,
        'coffee': 16,
        'money': 2.2,
    },
}

def get_coin_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a whole number.")

machine_is_on = True

while machine_is_on:
    choice = str(input("What would you like?\nEnter espresso, latte or cappuccino: "))
    while choice not in ['espresso', 'latte', 'cappuccino', 'off', 'report']:
        choice = str(input("Sorry, you can't have that.\nEnter espresso, latte or cappuccino: "))

    if choice == 'off':
        machine_is_on = False
    elif choice == 'report':
        print(f"Water: {resource_values['water']}ml\nMilk: {resource_values['milk']}ml\nCoffee: {resource_values['coffee']}g\nMoney: £{format(resource_values['money'], '.2f')}")
    elif choice in ['espresso','latte','cappuccino']:
        coffee = choice
        enough_resources = True
        for key, value in list(resource_values.items())[:-1]:
            if value < requirements[coffee][key]:
                print(f"Sorry, there isn't enough {key}")
                enough_resources = False
                break
        if not enough_resources:
            continue
        
        cash = [
            get_coin_input("How many pound coins will you insert? "),
            get_coin_input("How many 50p coins will you insert? "),
            get_coin_input("How many 20p coins will you insert? "),
            get_coin_input("How many 10p coins will you insert? ")
            ]
        cash_total = 1*cash[0] + 0.5*cash[1] + 0.2*cash[2] + 0.1*cash[3]

        if cash_total < requirements[coffee]['money']:
            print("Sorry, that's not enough money. Money refunded.")
        elif cash_total >= requirements[coffee]['money']:
            if cash_total > requirements[coffee]['money']:
                change = cash_total - requirements[coffee]['money']
                print(f"Here's £{format(change, '.2f')} in change.")
                resource_values['money'] += (cash_total - change)
            else:
                resource_values['money'] += cash_total
            resource_values['milk'] -= requirements[coffee]['milk']
            resource_values['coffee'] -= requirements[coffee]['coffee']
            resource_values['water'] -= requirements[coffee]['water']
            print(f"Here is your {coffee}. Enjoy!")