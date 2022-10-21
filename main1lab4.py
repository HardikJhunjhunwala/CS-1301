# Prolog
# Author: Hardik Jhunjhunwala
# Email: hjhunjhunwala1@student.gsu.edu
# Section: 22

num1 = int(input("Enter first number: "))   # Takes input from user for first integer.
num2 = int(input("Enter second number: "))  # Takes input from user for first integer.
num3 = int(input("Enter third number: "))   # Takes input from user for first integer.

if num1 < num2 and num1 < num3:      # Finding if the first number is the smallest.
    print(num1)                      # Printing the output.
elif num2 < num3 and num2 < num1:    # Finding if the second number is the smallest.
    print(num2)                      # Printing the output.
elif num3 < num1 and num3 < num2:    # Finding if the third number is the smallest.
    print(num3)                      # Printing the output.