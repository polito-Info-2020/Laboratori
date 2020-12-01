#
#  Compute the alternating sum of a list of values.
#

def main():
    # Read values from the user and store them in a list.
    values = []
    inputStr = input("Enter values (blank line to quit): ")
    while inputStr != "":
        values.append(float(inputStr))
        inputStr = input("Enter values (blank line to quit): ")

    # Display the alternating sum of the entered values.
    print("The alternating sum is", alternatingSum(values))

    # Shortcut: use the "sum" function over the slice composed of even-position
    # and odd-position elements, separately.
    print('Another way of computing the alternating sum:', sum(values[0::2]) - sum(values[1::2]))


# Compute the alternating sum of a list of values.
#  @param data the list of values to process
#  @return the alternating sum of the provided values
#
def alternatingSum(data):
    total = 0
    for i in range(len(data)):
        if i % 2 == 0:
            total = total + data[i]
        else:
            total = total - data[i]

    return total


# Call the main function.
main()
