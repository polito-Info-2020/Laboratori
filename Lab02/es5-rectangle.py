##
#  Compute the area, perimeter and diagonal length for a rectangle.
#
from math import sqrt

# Save the length and the width of the rectangle in two constant variables
LENGTH = 20.0
WIDTH = 35.0

# Alternatively, read the length and width from the user.
# length = float(input("Enter the length: "))
# width = float(input("Enter the width: "))

# Compute the area, perimeter and diagonal length.
area = LENGTH * WIDTH
perimeter = 2 * LENGTH + 2 * WIDTH
diagonal = sqrt(LENGTH * LENGTH + WIDTH * WIDTH)

# Display the result.
print("The area is", area)
print("The perimeter is", perimeter)
print("The diagonal length is %.2f" % diagonal)
