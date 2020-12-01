##
#  Display a square and a diamond with a side length supplied by the user.
#

# Read the side length from the user.
sideLength = int(input("Enter the side length: "))

# Display the square
for y in range(0, sideLength):
    print('*' * sideLength)
print()

# Display the diamond.
for y in range(1, sideLength):
    print(" " * (sideLength - y) + "*" * (y * 2 - 1))
for y in range(sideLength, 0, -1):
    print(" " * (sideLength - y) + "*" * (y * 2 - 1))
