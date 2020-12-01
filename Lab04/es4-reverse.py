##
#  Read a word from the user, and display its characters in reverse order.
#

# Read input from the user.
inputStr = input("Enter a word: ")

# Add each character to the beginning of the reversed string.
reverse = ""
for ch in inputStr:
    reverse = ch + reverse

# Display the result.
print(inputStr, "reversed is", reverse)
