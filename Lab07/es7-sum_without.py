##
#  Sum values without including the smallest.
#

# Define constants.
ONE_TEN = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def main():
    print("The sum without the smallest is", sumWithoutSmallest(ONE_TEN))


# Sum all elements in the list, excluding the smallest.
#  @param data the list of values to process
#  @return the sum of all of the values, excluding the smallest
#
def sumWithoutSmallest(data):
    smallest = data[0]
    total = 0

    for value in data:
        if value < smallest:
            smallest = value
        total = total + value

    return total - smallest


# Call the main function.
main()
