# Prolog
# Author: Hardik Jhunjhunwala
# Email: hjhunjhunwala1@student.gsu.edu
# Section: 22


def laps_to_miles(user_laps):     # Defines function laps_to_miles(user_laps)
    return(user_laps*0.25)        # Each lap is 0.25 miles thus value to be returned is number of laps multiplied by 0.25

if __name__=='__main__':
    user_laps = float(input('What is the number of laps? '))     # Takes input from user for number of laps
    number_of_miles = laps_to_miles(user_laps)                   # Assigns the variable number_of_miles the value found using the function laps_to_miles(user_laps)
    print(f'{number_of_miles:.2f}')                              # Prints the final value with required number of decimal places