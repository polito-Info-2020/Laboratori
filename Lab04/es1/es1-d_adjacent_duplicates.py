##
#   Find the adjacent duplicates in the values entered by the user.
#

# Read the first value from the user, and save it as the previous value.
inputStr = input("Enter an integer (blank line to quit): ")
prev = inputStr

# Check each value read from the user.   
printed = False
while inputStr != "":
    inputStr = input("Enter an integer (blank line to quit): ")

    # If it matches the previous value and we have not already printed that the
    # value is a duplicate then display an appropriate message.
    if prev == inputStr and not printed:
        print(inputStr, "is a duplicate.")
        printed = True
    if prev != inputStr:
        printed = False

    prev = inputStr
