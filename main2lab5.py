# Prolog
# Author: Hardik Jhunjhunwala
# Email: hjhunjhunwala1@student.gsu.edu
# Section: 22

''' Read in first equation, ax + by = c '''
a = int(input())                                    # Taking input of the value of 'a' in expression.
b = int(input())                                    # Taking input of the value of 'b' in expression.
c = int(input())                                    # Taking input of the value of 'c' in expression.
''' Read in second equation, dx + ey = f '''
d = int(input())                                    # Taking input of the value of 'd' in expression.
e = int(input())                                    # Taking input of the value of 'e' in expression.
f = int(input())                                    # Taking input of the value of 'f' in expression.
flag = 0
for x in range (-10, 10):                           # Taking range of x as -10 to 10 to test for possible solutions.
    for y in range (-10, 10):                       # Taking range of y as -10 to 10 to test for possible solutions.
        if a*x + b*y - c == d*x + e*y - f == 0:     # Checking if any possible values of x and y in -10 to 10 make the value of both equations zero and equal.
            print ("x = " , x , "," , "y = " , y)         # Printing value of x and y that was found from previous calculations.
            flag = 1
            break
if flag == 0:
    print("There is no solution.")                  # If no solution is found in that range then this statement is printed.
