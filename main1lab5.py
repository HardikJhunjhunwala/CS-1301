# Prolog
# Author: Hardik Jhunjhunwala
# Email: hjhunjhunwala1@student.gsu.edu
# Section: 22

int1 = int(input("Enter the first integer: "))                         # Taking input of value of first integer.
int2 = int(input("Enter the second integer: "))                        # Taking input of value of second integer.

if int1 < int2:                                                        # Since it is explictly mentioned that second integer cannot be less than first.
    print(int1, int1 + 5, int1 + 10, int1 + 15, int1 + 20, int1 + 25)  # If the condition is met this print statement prints the required values.
else:
    print("Second integer can't be less than the first.")               # If the condition is not met this prints the required error statement.