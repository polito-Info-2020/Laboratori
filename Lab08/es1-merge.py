#
#  Merge two sorted lists, with alternating elements from each list.
#

def main():
    # Set up sample lists.
    a = [1, 4, 9, 16]
    b = [9, 7, 4, 9, 11, 0]

    # Demonstrate that merge works correctly.
    print("List a is", a)
    print("List b is", b)
    result = merge(a, b)
    print("The merged list is", result)

    print("With reversed order:")
    result = merge(b, a)
    print("The merged list is", result)


def merge(a, b):
    """
    Merge two lists, alternating elements from each

    :param a: the first list to take elements from
    :param b: the second list to take elements from
    :return: the merged list
    """
    result = []

    # Merge elements from both lists as long as there are elements in both.
    len_shorter = min(len(a), len(b))
    for i in range(0, len_shorter):
        result.append(a[i])
        result.append(b[i])

    # Add the remaining elements from whichever list was longer.
    # Note: one of the two 'for' loops will NOT be executed, because either a or b has
    # already run out of elements.
    # If they have the same length, then no loop is executed, at all.
    for i in range(len_shorter, len(a)):
        result.append(a[i])
    for i in range(len_shorter, len(b)):
        result.append(b[i])

    return result


# Call the main function.
main()
