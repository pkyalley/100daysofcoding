# Instructions
    # Congratulations, you've got a job at Python Pizza!
    # Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill.
    # Small pizza (S): $15

    # Medium pizza (M): $20

    # Large pizza (L): $25

    # Add pepperoni for small pizza (Y or N): +$2

    # Add pepperoni for medium or large pizza (Y or N): +$3

    # Add extra cheese for any size pizza (Y or N): +$1

# Example Input
    # L
    # Y
    # N
# Example Output
    # Thank you for choosing Python Pizza Deliveries!
    # Your final bill is: $28.

print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

# Solution:

S = 15
M = 20
L = 25

PSP = 2
PMP = 3
PLP = 3

CS = 1
CM = 1
CL = 1

if size == "s".upper() and add_pepperoni == "y".upper() and extra_cheese == "y".upper():
  final_cost_for_small = S + PSP + CS
  print(f"Your final bill is: ${final_cost_for_small}.")
elif size == "s".upper() and add_pepperoni == "y".upper() and extra_cheese == "n".upper():
  final_cost_for_small = S + PSP
  print(f"Your final bill is: ${final_cost_for_small}.")
elif size == "s".upper() and add_pepperoni == "n".upper() and extra_cheese == "n".upper():
  final_cost_for_small = S
  print(f"Your final bill is: ${final_cost_for_small}.")
elif size == "s".upper() and add_pepperoni == "n".upper() and extra_cheese == "y".upper():
  final_cost_for_small = S + CS
  print(f"Your final bill is: ${final_cost_for_small}.")

if size == "m".upper() and add_pepperoni == "y".upper() and extra_cheese == "y".upper():
  final_cost_for_medium = M + PMP + CM
  print(f"Your final bill is: ${final_cost_for_medium}.")
elif size == "m".upper() and add_pepperoni == "y".upper() and extra_cheese == "n".upper():
  final_cost_for_medium = M + PMP
  print(f"Your final bill is: ${final_cost_for_medium}.")
elif size == "m".upper() and add_pepperoni == "n".upper() and extra_cheese == "n".upper():
  final_cost_for_medium = M
  print(f"Your final bill is: ${final_cost_for_medium}.")
elif size == "m".upper() and add_pepperoni == "n".upper() and extra_cheese == "y".upper():
  final_cost_for_medium = M + CM
  print(f"Your final bill is: ${final_cost_for_medium}.")

if size == "l".upper() and add_pepperoni == "y".upper() and extra_cheese == "y".upper():
  final_cost_for_large = L + PLP + CL
  print(f"Your final bill is: ${final_cost_for_large}.")
elif size == "l".upper() and add_pepperoni == "y".upper() and extra_cheese == "n".upper():
  final_cost_for_large = L + PLP
  print(f"Your final bill is: ${final_cost_for_large}.")
elif size == "l".upper() and add_pepperoni == "n".upper() and extra_cheese == "n".upper():
  final_cost_for_large = L
  print(f"Your final bill is: ${final_cost_for_large}.")
elif size == "l".upper() and add_pepperoni == "n".upper() and extra_cheese == "y".upper():
  final_cost_for_large = L + CL
  print(f"Your final bill is: ${final_cost_for_large}.")

# Facilitor's Solution:

bill = 0
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is: ${bill}.")

# Another Approach:

# Define base prices
prices = {'S': 15, 'M': 20, 'L': 25}

# Define additional costs
pepperoni_cost = {'S': 2, 'M': 3, 'L': 3}
cheese_cost = 1

# Calculate the final cost
final_cost = prices[size.upper()]

if add_pepperoni.upper() == 'Y':
    final_cost += pepperoni_cost[size.upper()]

if extra_cheese.upper() == 'Y':
    final_cost += cheese_cost

print(f"Your final bill is: ${final_cost}.")