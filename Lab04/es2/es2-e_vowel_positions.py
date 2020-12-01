##
#  Print the positions of all of the vowels in the string.
#

# Read input from the user.
inputStr = input("Enter a string: ")

# Check each character.  If it is a vowel display its position.
print("The vowels are at positions: ", end="")
for i in range(0, len(inputStr)):
    if inputStr[i] in "aeiouAEIOU":
        print(i+1, end=" ")

print()
