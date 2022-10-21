# Prolog
# Author: Hardik Jhunjhunwala
# Email: hjhunjhunwala1@student.gsu.edu
# Section: 22

def days_in_feb(user_year):                                           # Defines a function days_in_feb to output the number of days in February for a given year.
    if user_year % 4 != 0:                                            # Divides the value of year by 4 to check if it divisible by 4.
        return(f'{user_year} has 28 days in February.')               # If the year doesnt give a remainder of 0 it is printed as a non-leap year.
    else:                                                             # If the year gives a remainder if 0 it is passed through more statements to verify if it is a leap year.
        if user_year % 100 == 0:                                      # If the year doesn't give a remainder while being divided by 100 it is a century year and if further checked.
            if user_year % 400 != 0:                                  # If the century year gives a non-zero number after being divided by 400 it is not a leap year.
                return(f'{user_year} has 28 days in February.')       # The century year is printed as a non-leap year.
            else:                                                     # If the century year gives zero as the remainder after being divided by 400 it is a leap year.
                return(f'{user_year} has 29 days in February.')       # The century year is printed as a leap year.
        else:                                                         # If the year gives a non-zero number as a remainder after being divided by 100 it is not a century year but is a leap year since it was divisible by 4.
            return(f'{user_year} has 29 days in February.')           # The year is printed as a leap year since it was divisible by 4.


if __name__ == '__main__':
    year = int(input("What is the year? "))       # Takes input from the user for what year is to bbe checked.
    print(days_in_feb(year))                      # Prints the final answer after running the above function with the user inputed value for year.