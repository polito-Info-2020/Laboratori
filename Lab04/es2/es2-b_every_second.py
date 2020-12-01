##
#  Print every second letter in a string.
#

# Read input from the user.
inputStr = input("Enter a string: ")

# Display every second letter.
for i in range(1, len(inputStr), 2):
    print(inputStr[i], end='')

print()
