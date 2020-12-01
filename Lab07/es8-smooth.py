##
#  Smooth out values in a list by averaging them with their neighbors.
#

def main():
    values = [1, 2, 3, 5, 3, 1, 4]

    # Display the original values.
    print("The original values are:", values)

    # Smooth the values and display the result.
    smooth(values)
    print("The smoothed values are:", values)


# Smooth values in a list by average the value with its neighbor(s).
#  @param data the list of values to smooth
#
def smooth(data):
    if len(data) <= 1:
        return

    # Handle the first element in the list.
    old_left = data[0]
    data[0] = (data[0] + data[1]) / 2

    # Handle all values except for the first and last.
    for i in range(1, len(data) - 1):
        current = data[i]
        data[i] = (old_left + data[i] + data[i + 1]) / 3
        old_left = current

    # Handle the last element in the list.
    data[len(data) - 1] = (old_left + data[len(data) - 1]) / 2


# Call the main function.
main()
