##
#  Generate random integers and display them in different ways.
#
from random import randint

# Define constants.
NUM_INTEGERS = 10
MAX_VALUE = 100

# Generate the random integers from 1 to MAX_VALUE
values = []
for i in range(0, NUM_INTEGERS):
    values.append(randint(1, MAX_VALUE))

# Display the elements at even index.
print("Elements at even index: ", end="")
for i in range(0, len(values), 2):
    print(values[i], end=" ")
print()

# Display the even elements.
# Alternative 1: use a for..range loop
print("The even elements are: ", end="")
for i in range(0, len(values)):
    if values[i] % 2 == 0:
        print(values[i], end=" ")
print()

# Alternative 2: usa a for..in statement
print("The even elements are: ", end="")
for num in values:
    if num % 2 == 0:
        print(num, end=" ")
print()


# Display the elements in reverse order.
print("In reverse order:")
for i in range(len(values) - 1, -1, -1):
    print(values[i], end=" ")
print()

# Display the first and last element.
print("First and last:", values[0], values[len(values) - 1])
print("First and last:", values[0], values[-1])  # shortcut: negative index
