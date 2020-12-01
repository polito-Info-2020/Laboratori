##
#  Convert from Roman numerals to a decimal number.
#

def main():
    print(romanToDecimal("I"))
    print(romanToDecimal("MCMLXXVIII"))
    print(romanToDecimal("MMMCMXCIX"))


#  Convert a string of Roman numerals to decimal.
#  @param r the string of numerals to convert
#  @return the decimal equivalent of r
#
def romanToDecimal(r):
    total = 0
    while r != "":
        if len(r) == 1 or convertDigit(r[0]) >= convertDigit(r[1]):
            total = total + convertDigit(r[0])
            r = r[1:]  # eliminate 1st character
        else:
            total = total + (convertDigit(r[1]) - convertDigit(r[0]))
            r = r[2:]  # eliminate 1st and 2nd characters
    return total


# Convert a single Roman numeral character to decimal.
#  @param r the character to convert
#  @return the decimal equivalent of r
#
def convertDigit(r):
    if r == "I":
        return 1
    if r == "V":
        return 5
    if r == "X":
        return 10
    if r == "L":
        return 50
    if r == "C":
        return 100
    if r == "D":
        return 500
    if r == "M":
        return 1000


# Call the main function.
main()
