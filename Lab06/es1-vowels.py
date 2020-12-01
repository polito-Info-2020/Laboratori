##
#  Use a function to count the number of vowels in a string.
#

def main():
    inputStr = input("Enter a string: ")
    print("The string contains", countVowels(inputStr), "vowels")


# Count the number of vowels in a string.
#  @param string the string of characters to process
#  @return the number of vowels
#
def countVowels(string):
    count = 0
    for ch in string:
        if ch.upper() in "AEIOU":
            count = count + 1
    return count


# Call the main function.
main()
