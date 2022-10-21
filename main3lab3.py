# Prolog
# Author: Hardik Jhunjhunwala
# Email: hjhunjhunwala1@student.gsu.edu
# Section: 22

amount = int(input("What is the given caffeine amount? "))  # Takes input from user of amount of caffeine originally present.

# Half life of caffeine is given as 6 hours which implies after every 6 hours the amount of caffeine becomes half of the previous value.

hour6 = amount / 2      # Going by half life logic after 6 hours amount of caffeine will become half of the original value.
hour12 = hour6 / 2      # Going by half life logic after 12 hours amount of caffeine will become a fourth of the original value or half of the value it had after 6 hours.
hour24 = hour12 / 4    # Going by half life logic after 24 hours amount of caffeine will become a sixteenth of the original value or a fourth of the value it had after 125 hours.

print("After 6 hours: ", f'{hour6:.2f}','mg')    # Prints amount of caffeine after 6 hours.
print("After 12 hours: ", f'{hour12:.2f}','mg')  # Prints amount of caffeine after 12 hours.
print("After 24 hours: ", f'{hour24:.2f}','mg')  # Prints amount of caffeine after 24 hours.