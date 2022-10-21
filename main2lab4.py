# Prolog
# Author: Hardik Jhunjhunwala
# Email: hjhunjhunwala1@student.gsu.edu
# Section: 22

num = int(input("What is the highway number? "))      #Taking input from user for the highway number. 

if num % 100 != 00 and num % 2 == 0:      # Checking if the number is even and doesn't end with two zeros.
    if num  // 100 !=0:                   # Checking if the number has a third digit.
        print("I-"+ str(num) , " is auxiliary, serving I-"+ str(num % 100)," going east/west.")  # Using string conversion and concatination the unnecessary spaces are removed and final answer is printed.
    else:                                 # If the number doesn't have three digits it is not a auxiliary highway and is printed as a primary highway.
        print("I-"+ str(num) ," is primary, going east/west")  # Using string conversion and concatination the unnecessary spaces are removed and final answer is printed.
elif num % 100 != 00 and num % 5 == 0:    # Checking if the number is odd and doesn't end with two zeros.
    if num  // 100 !=0:                   # Checking if the number has a third digit.
        print("I-"+ str(num) , " is auxiliary, serving I-"+ str(num % 100)," going north/south.")  # Using string conversion and concatination the unnecessary spaces are removed and final answer is printed.
    else:                                 # If the number doesn't have three digits it is not a auxiliary highway and is printed as a primary highway.
        print("I-"+ str(num) ," is primary, going north/south")   # Using string conversion and concatination the unnecessary spaces are removed and final answer is printed.
elif num % 100 == 00:                     # Highway number ending in two zeros (00) is invalid.
    print(str(num)+" is not a valid interstate highway number. ")  # Using string conversion and concatination the unnecessary spaces are removed and final answer is printed.