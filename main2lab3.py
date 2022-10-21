# Prolog
# Author: Hardik Jhunjhunwala
# Email: hjhunjhunwala1@student.gsu.edu
# Section: 22

number = int(input("What is the phone number? "))  # Takes the number input from the user

last4 = number % 10000                            # Gets the last four digits of the number.
middle3 = int(((number -last4)/10000)%1000)       # Gets the middle 3 digits of the number by subtracting the last four digits and dividing by 10000 to remove the last 4 digits.
first3 = number//10000000                         # Gets the first 3 digits of the number by doing integer division.


last4 = str(last4)                     # Converts the numbers from integer type to string type.
middle3 = str(middle3)                 # Converts the numbers from integer type to string type.
first3 = str(first3)                   # Converts the numbers from integer type to string type.


print('('+first3+')'+middle3+'-'+last4) # Prints the output in the required format by using string concatination to position the brackets and dash correctly.