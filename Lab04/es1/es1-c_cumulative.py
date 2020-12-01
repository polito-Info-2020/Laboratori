##
#  Display the cumulative totals of the values entered by the user.
#

# Read input from the user.
inputStr = input("Enter an integer (blank line to quit): ")

# Add each value to the total as it is read, and display the cumulative total.
total = 0
while inputStr != "":
    value = int(inputStr)
    total = total + value
    print("The cumulative total is", total)

    inputStr = input("Enter an integer (blank line to quit): ")
