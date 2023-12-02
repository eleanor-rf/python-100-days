logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add (num1,num2):
    return num1 + num2
def subtract (num1,num2):
    return num1 - num2
def divide (num1,num2):
    return num1 / num2
def multiply (num1,num2):
    return num1 * num2

map = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,
}

print(logo)

number1 = float(input("Enter the first number: "))

finished = False

while not finished:
    operator = input("Choose an operation: + - / *: ")
    number2 = float(input("Enter the next number: "))
    function = map[operator]
    result = function(number1,number2)
    print(f"{number1} {operator} {number2} = {result}")
    number1 = result
    continue_calc = input("Type 'y' to continue, 'n' to start a new calculation, or 'exit' to exit: ")

    if continue_calc == 'y':
        print(f"Current number: {number1}")
    elif continue_calc == 'n':
        number1 = float(input("Enter the first number: "))
    elif continue_calc == 'exit':
        finished = True