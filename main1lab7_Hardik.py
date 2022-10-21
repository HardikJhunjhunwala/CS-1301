# Prolog
# Author: Hardik Jhunjhunwala
# Email: hjhunjhunwala1@student.gsu.edu
# Section: 22

def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):     # Defining a function driving_cost. 
    gallons = miles_driven/miles_per_gallon                               # Calculating number of gallons.
    cost = gallons * dollars_per_gallon                                   # Calculating cost for number of gallons.
    return cost                                                           # Returns value of final cost.


miles_per_gallon = float(input('How many miles per gallon?'))             # Takes input of number of miles per gallon from user.
dollars_per_gallon = float(input('How many dollars per gallon?'))         # Takes input of number of dollars per gallon from user.

print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, 10):.2f}')    # Prints cost of driving for 10 miles by recalling the function.
print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, 50):.2f}')    # Prints cost of driving for 50 miles by recalling the function.
print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, 400):.2f}')   # Prints cost of driving for 400 miles by recalling the function.