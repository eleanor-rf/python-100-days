print("Welcome to the tip calculator.")
total = float(input("What was the total bill? "))
percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

per_person = ((percentage/100)*total + total) / people
rounded_per_person = "{:.2f}".format(per_person)

print(f"Each person should pay: £{rounded_per_person}") 