##
#  Determine if two lists contain the same values in any order, ignoring 
#  duplicates.
#

# Define constants.
LIST_1 = [1, 4, 9, 16, 9, 7, 4, 9, 11]
LIST_2 = [11, 11, 7, 9, 16, 4, 1]


def main():
    print("List 1 is", LIST_1)
    print("List 2 is", LIST_2)
    print("The lists contain the same elements: ", sameSet(LIST_1, LIST_2))


# Determine if two lists contain the same elements in any order, ignoring
#  duplicates.
#  @param l1 the first list to consider
#  @param l2 the second list to consider
#  @return True if the lists contain the same elements, False otherwise
#
def sameSet(l1, l2):
    for value in l1:
        if value not in l2:
            return False

    for value in l2:
        if value not in l1:
            return False

    return True


# Call the main function.
main()
