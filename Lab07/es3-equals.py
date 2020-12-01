##
#  Determine if 2 lists are equal.
#

# Define constants.
LIST_1 = [1, 2, 3]
LIST_2 = [1, 2, 3]


def main():
    print("List 1 is", LIST_1)
    print("List 2 is", LIST_2)
    print("List 1 and List 2 are equal: ", equalsOneByOne(LIST_1, LIST_2))


# Determine if two lists have the same elements in the same order.
#  @param l1 the first list to consider
#  @param l2 the second list to consider
#  @return True if the lists are the same, otherwise False
#
def equalsOneByOne(l1, l2):
    equal = True
    if len(l1) == len(l2):
        i = 0
        while i < len(l1) and equal:
            # If an element at the i position in the first list is different
            # from the element in such position in the second list, the iteration
            # is stopped by setting 'equal' to false.
            if l1[i] != l2[i]:
                equal = False
            i = i + 1
    else:
        equal = False

    return equal


# Shortcut: in Python the '==' comparison operator already checks whether the two lists
# contain the same elements in the same order

# Determine if two lists have the same elements in the same order.
#  @param l1 the first list to consider
#  @param l2 the second list to consider
#  @return True if the lists are the same, otherwise False
#
def equals(l1, l2):
    return l1 == l2


# Call the main function.
main()
