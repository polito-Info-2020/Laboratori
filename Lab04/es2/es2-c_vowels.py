##
#  Print a string where the vowels have been replaced with underscores.
#

# Read input from the user.
inputStr = input("Enter a string: ")

# Check each character.  If it is a vowel display an underscore instead of
# the character.
for ch in inputStr:
    if ch in "aeiouAEIOU":  # or: ch.lower() in "aeiou"
        print("_", end="")
    else:
        print(ch, end="")

print()
