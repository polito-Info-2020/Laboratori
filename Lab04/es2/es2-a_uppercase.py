##
#  Print the uppercase letters in a string.
#

# Read input from the user.
inputStr = input("Enter a string: ")

# Find and display the uppercase letters.
for ch in inputStr:
    if "A" <= ch <= "Z":    # or: ch >= "A" and ch <= "Z"
        print(ch, end="")

print()
