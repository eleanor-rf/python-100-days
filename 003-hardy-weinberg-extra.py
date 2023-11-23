# Hardy-Weinberg calculator for A Level

import math
import sys

known_var = input("What do you know? p, q, p^2, q^2 or (p^2 + 2pq)? ")
if known_var in ["p", "q", "p^2", "q^2", "p^2 + 2pq", "(p^2 + 2pq)"]:
  value = float(input("Enter the value as a decimal: "))
else:
  sys.exit("Didn't understand input, sorry.")

if 0 < value < 1:
  if known_var == "p":
    p = value
    q = 1 - value
    print(f"q = {q}\np^2 = {value**2}\nq^2 = {q**2}\n2pq = {2*p*q}")
  elif known_var == "q":
    q = value
    p = 1 - value
    print(f"p = {p}\np^2 = {p**2}\nq^2 = {q**2}\n2pq = {2*p*q}")
  elif known_var == "p^2":
    p = math.sqrt(value)
    q = 1 - value
    print(f"p = {p}\nq = {q}\nq^2 = {q**2}\n2pq = {2*p*q}")
  elif known_var == "q^2":
    q = math.sqrt(value)
    p = 1 - value
    print(f"p = {p}\nq = {q}\np^2 = {p**2}\n2pq = {2*p*q}")
  elif known_var in ["(p^2 + 2pq)", "p^2 + 2pq"]:
    q_squared = 1 - value
    q = math.sqrt(q_squared)
    p = 1 - q
    print(f"p = {p}\nq = {q}\np^2 = {p**2}\nq^2 = {q**2}\n2pq = {2*p*q}")
else:
  sys.exit("Error: Expected a positive decimal.")

next = input("Do you want to calculate numbers of individuals?: Y or N: ").lower()

if next == "y":
  pop_size = int(input("What is the population size? Enter a number: "))
  print(f"Number of homozygous dominant = {round(pop_size*p**2)}")
  print(f"Number of heterozygotes = {round(pop_size*2*p*q)}")
  print(f"Number of homozygous recessive = {round(pop_size*q**2)}")
else:
  sys.exit("Ok, bye :-)")