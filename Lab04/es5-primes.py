##
#  Compute and display all of the prime numbers up to an integer entered by
#  the user.
#

from math import sqrt

# Read the upper limit from the user.
limit = int(input("Enter an integer: "))

# Check each integer from 2 to limit, displaying it if it is prime.
for num in range(2, limit + 1):
    isPrime = True

    # Check each number up to sqrt(num) to see if it divides into num.
    for factor in range(2, round(sqrt(num)) + 1):
        if num % factor == 0:
            isPrime = False

    if isPrime:
        print(num)
