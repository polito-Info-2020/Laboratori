##
#  Determine if one string is within another.
#  Note: this is equivalent to: `` if match in string: ``
#
def main():
    print("find(\"Mississippi\", \"sip\") returned", find("Mississippi", "sip"))
    print("find(\"Mississippi\", \"sips\") returned", find("Mississippi", "sips"))
    print("find(\"Mississippi\", \"Mi\") returned", find("Mississippi", "Mi"))
    print("find(\"Mississippi\", \"pi\") returned", find("Mississippi", "pi"))
    print("find(\"Mississippi\", \"p\") returned", find("Mississippi", "p"))
    print("find(\"Mississippi\", \"q\") returned", find("Mississippi", "q"))


## Determine if match occurs anywhere in the string.
#  @param string the string to search
#  @param match the string that we are looking for
#  @return True if match occurs anywhere in string, otherwise False
#
def find(string, match):
    # string =   c c c c c c c c c c c c c
    #                | | | |
    # match =        m m m m

    # The idea is to try to check if "mmmm" is equal to a PORTION of the string.
    # We must try to position the "mmmm" in all possible starting points

    # The starting point goes from 0 (flushed left) to len(string)-len(match)+1 (flushed right)

    found = False
    for start in range(0, len(string) - len(match) + 1):
        if find_starting_from(string, match, start):
            found = True
    return found


# Check if the characters in 'string', starting at position 'start'
# are equal to the characters in 'match', starting at position 0
# Note: equivalent to: `` if string[start, start+len(match)]==match: ``
def find_starting_from(string, match, start):
    # check all characters
    differ = False
    for i in range(len(match)):
        if match[i] != string[start + i]:
            differ = True
    return not differ


# Call the main function.
main()
