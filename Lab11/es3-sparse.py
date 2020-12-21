##
#  Compute the sum of two sparse arrays stored in dictionaries.
#

def main():
    a = {5: 4, 9: 2, 10: 9}
    b = {5: 4, 8: 4, 10: 4}

    print("a is", a)
    print("b is", b)
    print("The sum of a and b is:", sparseArraySum(a, b))


## Compute the sum of two sparse arrays.
#  @param a the first array to include in the sum
#  @param b the second array to include in the sum
def sparseArraySum(a, b):
    retval = dict(a)
    for key in b:
        if key in retval:
            retval[key] = retval[key] + b[key]
        else:
            retval[key] = b[key]
    return retval


# Call the main function.
main()
