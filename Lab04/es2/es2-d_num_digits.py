##
#  Count the number of digits in a string.
#

# Read input from the user.
inputStr = input("Enter a string: ")

# Check each character.  If it is a digit, add it to the count.
count = 0
for ch in inputStr:
    if ch.isdigit():  # or: "0" <= ch <= "9"
        count = count + 1

print("The string contains", count, "digits.")
