##
#  Determine if 3 numbers are in increasing order, decreasing order, or 
#  neither.
#

# Read three numbers from the user.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Determine and display their status.
if num1 < num2 and num2 < num3:
    print("They are in increasing order.")
elif num1 > num2 and num2 > num3:
    print("They are in decreasing order.")
else:
    print("They are neither in increasing order nor decreasing order.")

# NOTA: si può anche scrivere
# if num1 < num2 < num3:
