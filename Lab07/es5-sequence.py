##
#  Generate a random sequence of values, print it, sort it, and print it again.
#
from random import randint

# Define constants.
NUM_VALUES = 20
MIN_VALUE = 0
MAX_VALUE = 99

# Generate the list of random values.
values = []
for i in range(0, NUM_VALUES):
    values.append(randint(MIN_VALUE, MAX_VALUE))

# Display the original values.
print("The values are:")
print(values)

# Sort the values and display them again.
values.sort()
print("The values in sorted order are:")
print(values)
