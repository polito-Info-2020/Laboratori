##
#  Save a 5 digit integer in a constant, and then display it with spaces
#  between each digit.
#

NUM = 16384

# Alternatively, gather input from the user.
# NUM = int(input("Enter a 5 digit integer: "))

# Display the result.
num = str(NUM) 
print(num[0], num[1], num[2], num[3], num[4])

# Alternative solution: use divisions and remainders
n = NUM
dig0 = n % 10
n = n // 10
dig1 = n % 10
n = n // 10
dig2 = n % 10
n = n // 10
dig3 = n % 10
n = n // 10
dig4 = n % 10
print(dig4, dig3, dig2, dig1, dig0)
