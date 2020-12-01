##
#  Print the smallest and largest values entered by the user.  The user will
#  enter a blank line to quit.
#

# Read the first input value from the user.
inputStr = input("Enter an integer (blank line to quit): ")

# If the first value was an integer, process it and the remaining input values.
# Otherwise an appropriate error message is displayed.
if inputStr != "":
    value = int(inputStr)
    smallest = value
    largest = value

    # As long as the user hasn't entered a blank line, convert the input to an
    # integer and determine if it is a new smallest or largest value.
    while inputStr != "":
        value = int(inputStr)

        if value < smallest:
            smallest = value
        if value > largest:
            largest = value

        inputStr = input("Enter an integer (blank line to quit): ")

    # Display the results.
    print("The smallest value is", smallest, "and the largest value is", largest)

else:
    # Display an error message if no input values are provided.
    print("No input values were provided.")
