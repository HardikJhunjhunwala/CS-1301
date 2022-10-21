# Prolog
# Author: Hardik Jhunjhunwala
# Email: hjhunjhunwala1@student.gsu.edu
# Section: 22


def max_magnitude(user_val1, user_val2, user_val3):      # Defines a function max_magnitude(user_val1, user_val2, user_val3)
    val1 = abs(user_val1)                                # Converts value of user_val1 to positive number for finding number with hishest magnitude
    val2 = abs(user_val2)                                # Converts value of user_val2 to positive number for finding number with hishest magnitude
    val3 = abs(user_val3)                                # Converts value of user_val3 to positive number for finding number with hishest magnitude
    lst = [val1, val2, val3]                             # Makes a list of the values of number found above
    number = max(lst)                                    # Finds value of highest number in the list
    if number == val1:                                   # For negative values since they were made positive for finding magnitude
        return(user_val1)                                # Returns the value of the largest number by magnitude
    if number == val2:                                   # For negative values since they were made positive for finding magnitude
        return(user_val2)                                # Returns the value of the largest number by magnitude
    if number == val3:                                   # For negative values since they were made positive for finding magnitude
        return(user_val3)                                # Returns the value of the largest number by magnitude
if __name__ == '__main__':
    user_val1 = int(input("What is the first value? "))       # Takes input from user for first value
    user_val2 = int(input("What is the second value? "))      # Takes input from user for second value
    user_val3 = int(input("What is the third value? "))       # Takes input from user for third value
    maximum = max_magnitude(user_val1, user_val2, user_val3)     # Assigns the variable maximum with the value found from the function max_magnitude(user_val1, user_val2, user_val3)
    print(maximum)                                       # Prints the final value  