# Prolog
# Author: Hardik Jhunjhunwala
# Email: hjhunjhunwala1@student.gsu.edu
# Section: 22

symbol1 = input("What is the first symbol ? ")  # Takes the first symbol choice from the user.
symbol2 = input("What is the second symbol ? ") # Takes the second symbol shoice from the user.

line1 = ' ' * 6 + symbol2            # String concatinating 6 spaces and a hastag symbol. The power symbol helps in increasing the number of blanks to 6.
line2 = symbol1 * 6 + symbol2 * 2    # String concatinating 6 of symbol1 and 2 of symbol2. The power symbol helps in increasing the number of symbol1 to 6 and symbol2 to 2.
line3 = symbol1 * 6 + symbol2 * 3    # String concatinating 6 of symbol1 and 3 of symbol2. The power symbol helps in increasing the number of symbol1 to 6 and symbol2 to 3.
line4 = symbol1 * 6 + symbol2 * 2    # String concatinating 6 of symbol1 and 2 of symbol2. The power symbol helps in increasing the number of symbol1 to 6 and symbol2 to 2.
line5 = ' ' * 6 + symbol2            # String concatinating 6 spaces and a hastag symbol. The power symbol helps in increasing the number of blanks to 6.


print(line1) # Prints line1 from above.
print(line2) # Prints line2 from above.
print(line3) # Prints line3 from above.
print(line4) # Prints line4 from above.
print(line5) # Prints line5 from above.
