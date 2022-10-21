# Prolog
# Author: Hardik Jhunjhunwala
# Email: hjhunjhunwala1@student.gsu.edu
# Section: 22

def feet_to_steps(user_feet):     # Defining a function feet_to_steps to convert number of feet walked to number of steps.
    steps = user_feet/2.5         # Finds number of steps by dividing number of feet by 2.5 (number of feet covered in each step).
    step_int = int(steps)         # Converting the final answer to integer to eliminate decimal values.
    return step_int               # Returns the final value of number of steps walked to print it.

if __name__ == '__main__':
    feet = float(input("Enter number of feet walked: "))   # Takes input from user for the number of feet walked to use it in the function.
    print(feet_to_steps(feet))                             # Uses user given value and recalls the function and prints the final value.