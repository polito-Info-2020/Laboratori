##
#  Implement and demonstrate a collection of list functions.
#
from random import randint


def main():
    rand_list = [randint(1, 20) for i in range(10)]  # generate a list of 10 random numbers from 1 to 20
    print("The original data for all functions is: ", rand_list)

    # a) Demonstrate swapping the first and last element.
    data = list(rand_list)
    swapFirstLast(data)
    print("After swapping first and last: ", data)

    # b) Demonstrate shifting to the right.
    data = list(rand_list)
    shiftRight(data)
    print("After shifting right: ", data)

    # c) Demonstrate replacing even elements with zero.
    data = list(rand_list)
    replaceEven(data)
    print("After replacing even elements: ", data)

    # d) Demonstrate replacing values with the larger of their neighbors.
    data = list(rand_list)
    replaceNeighbors(data)
    print("After replacing with neighbors: ", data)

    # e) Demonstrate removing the middle element.
    data = list(rand_list)
    removeMiddle(data)
    print("After removing the middle element(s): ", data)

    # f) Demonstrate moving even elements to the front of the list.
    data = list(rand_list)
    evenToFront(data)
    print("After moving even elements: ", data)

    # g) Demonstrate finding the second largest value.
    print("The second largest value is: ", secondLargest(rand_list))

    # h) Demonstrate testing if the list is in increasing order.
    print("The list is in increasing order: ", isIncreasing(rand_list))

    # i) Demonstrate testing if the list contains adjacent duplicates.
    print("The list has adjacent duplicates: ", hasAdjacentDuplicate(rand_list))

    # j) Demonstrate testing if the list contains duplicates.
    print("The list has duplicates: ", hasDuplicate(rand_list))


def swapFirstLast(data):
    """
    Swap the first and last element in a list

    :param data: the list of values to process
    """
    if len(data) < 2:
        return
    (data[0], data[-1]) = (data[-1], data[0])

    # Alternate solution (without 'shortcuts')
    # temp = data[0]
    # data[0] = data[len(data) - 1]
    # data[len(data) - 1] = temp


def shiftRight(data):
    """
    Shift the elements to the right

    :param data: the list of values to process
    """
    if len(data) == 0:
        return

    last = data[len(data) - 1]
    # Iteration starting from the last element in the list and ending at the second one (i = 1)
    for i in range(len(data) - 1, 0, -1):
        data[i] = data[i - 1]
    data[0] = last

    # shortcut using slices and tuples
    # (data[0], data[1:]) = (data[-1], data[:-1])


def replaceEven(data):
    """
    Replace all even elements in the list with 0

    :param data: the list of values to process
    """
    for i in range(0, len(data)):
        if data[i] % 2 == 0:
            data[i] = 0


def replaceNeighbors(data):
    """
    Replace each value with the larger of its neighbors

    :param data:
    :return: the list of values to process
    """
    # Make a copy of the list
    old_values = list(data)
    for i in range(1, len(data) - 1):
        data[i] = max(old_values[i - 1], old_values[i + 1])


def removeMiddle(data):
    """
    Remove the middle element or elements from a list

    :param data: the list of values to process
    """
    if len(data) == 0:
        return

    if len(data) % 2 == 1:
        data.pop(len(data) // 2)
    else:
        data.pop(len(data) // 2)
        data.pop(len(data) // 2)


def evenToFront(data):
    """
    Move even elements to the front of the list

    :param data: the list of values to process
    """
    evenPos = 0
    pos = 0
    while pos < len(data):
        if data[pos] % 2 == 0:
            temp = data.pop(pos)
            data.insert(evenPos, temp)
            evenPos = evenPos + 1
        pos = pos + 1


def secondLargest(data):
    """
    Identify the second largest value in a list

    :param data: the list of values to process
    :return: the second largest value in the list
    """
    largest = max(data)
    secondLargest = min(data)  # just as an initial guess
    for value in data:
        if value > secondLargest and value != largest:
            secondLargest = value
    return secondLargest


def isIncreasing(data):
    """
    Determine whether or not the list is in increasing order

    :param data: the list of values to process
    :return: True if the list is in increasing order, False otherwise
    """
    increasing = True
    for i in range(0, len(data) - 1):
        if data[i] > data[i + 1]:
            increasing = False
    return increasing


def hasAdjacentDuplicate(data):
    """
    Determine if the list contains adjacent duplicate elements

    :param data: the list of values to process
    :return: True if the list contains adjacent duplicates, False otherwise
    """
    has_dup = False
    for i in range(0, len(data) - 1):
        if data[i] == data[i + 1]:
            has_dup = True
    return has_dup


def hasDuplicate(data):
    """
    Determine if the list contains duplicate elements

    :param data: the list of values to process
    :return: True if the list contains duplicates, False otherwise
    """
    hasDup = False
    for i in range(0, len(data) - 1):
        for j in range(i + 1, len(data)):  # avoid comparing data[i] with itself!!
            if data[i] == data[j]:
                hasDup = True
    return hasDup


# Call the main function.
main()
