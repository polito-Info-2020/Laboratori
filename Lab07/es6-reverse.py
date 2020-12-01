##
#  Reverse a list of values.
#

def main():
    # Demonstrate the reverse function.
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("The original data is", data)
    reverse(data)
    print("The reversed data is", data)


# Reverse the elements in a list.
#  @param data the list of elements to reverse
#
def reverse(data):
    for i in range(0, len(data) // 2):
        # swap elements in symmetrical positions: the i-th from the left with the i-th from the right
        temp = data[i]
        data[i] = data[len(data) - 1 - i]
        data[len(data) - 1 - i] = temp

        # Shortcut: swat 2 elements with 1 instruction, using tuples
        # (data[i], data[len(data) - 1 - i]) = (data[len(data) - 1 - i], data[i])


# Call the main function.
main()
