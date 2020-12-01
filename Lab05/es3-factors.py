##
#  Compute and display the factors of an integer.
#

# Read an integer from the user.
value = int(input("Enter an integer: "))

# Compute and display the factors.
print("The factors are:")
divisor = 2

while value > 1:

    # extract all occurrences of divisors
    # (the 'while' will iterate if the divisor has a power >1)
    while value % divisor == 0:
        print(divisor)
        value = value / divisor

    # when we finished the current divisor, go to the next one
    divisor = divisor + 1
