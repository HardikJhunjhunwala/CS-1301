num1 = int(input("Enter principal amount : "))
num2 = int(input("Enter interest rate : "))
rate = num2/100
interest = num1 * rate
final = num1 + interest
print("The interest is: ",interest)
print("The final amount is :",final)
