def split_check(bill, people, tax_percentage = 0.09, tip_percentage = 0.15):
    tax = bill * tax_percentage
    tip = bill * tip_percentage
    total = bill + tax + tip 
    amount_per_diner = total/people
    return amount_per_diner

bill = float(input("bill:   "))
people = int(input("people: "))

print('Cost per diner:', split_check(bill, people))

bill = float(input())
people = int(input())
new_tax_percentage = float(input())
new_tip_percentage = float(input())

print('Cost per diner:', split_check(bill, people, new_tax_percentage, new_tip_percentage))