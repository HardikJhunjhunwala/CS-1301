# Prolog
# Author: Hardik Jhunjhunwala
# Email: hjhunjhunwala1@student.gsu.edu
# Section: 22

lst = []                                                       # Creating an empty list so that the numbers can be appended into it.

n = int(input("Enter the number of values in the list: "))     # Taking Input of number of values in the list.

for i in range(0,n):                                           # 
    ele = float(input())                                       # Taking input of the numbers to be added to the list.
    lst.append(ele)                                            # Adding the number to the list

largest = max(lst)                                             # Taking value of the largest number from the list.

for i in lst:                                                  # Taking each element from the list to perform the required operations on it.
    i = i/largest                                              # Dividing each element by the largest value from the list.        
    print(f'{i:.2f}')                                          # Printing the value of the elements after division.