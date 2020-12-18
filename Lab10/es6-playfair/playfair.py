##
#  Implement the playfair cipher.
#

def main():
    # Gather input from the user.
    keyword = removeDuplicates(input("Enter the keyword: ").upper())
    in_name = input("Enter the input file name: ")
    out_name = input("Enter the output file name: ")

    # Read all of the text out of the file.
    inf = open(in_name, "r")
    text = inf.read()
    inf.close()

    # I's and J's are considered the same, so replace all J's with I's.
    text = text.replace("J", "I")

    # Ensure we have an even number of letters by padding with a Z.
    count = 0
    for ch in text:
        if ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
            count = count + 1

    if count % 2 == 1:
        text = text + "Z"

    # I's and J's are considered the same, so replace all J's with I's.
    keyword = keyword.replace("J", "I")

    # Create the table for modifying the text.
    table = createTable(keyword)

    # Perform the transformation.
    result = ""
    i = 0
    while i < len(text):
        before = ""
        between = ""
        after = ""

        while i < len(text) and text[i] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
            before = before + text[i]
            i = i + 1

        (r1, c1) = getPos(text[i], table)
        i = i + 1

        while i < len(text) and text[i] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
            between = between + text[i]
            i = i + 1

        (r2, c2) = getPos(text[i], table)
        i = i + 1

        while i < len(text) and text[i] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
            after = after + text[i]
            i = i + 1

        # Handle two letters in the same row.
        if r1 == r2:
            result = result + before + table[r1][c2] + between + table[r2][c1] + after
        # Handle two letters in the same column.
        elif c1 == c2:
            result = result + before + table[r2][c2] + between + table[r1][c1] + after
        # Handle all other cases.
        else:
            result = result + before + table[r1][c2] + between + table[r2][c1] + after

    # Save the result.
    outf = open(out_name, "w")
    outf.write(result)
    outf.close()


## Find the row and column in which a letter exists in a table.
#  @param letter the letter to search for
#  @param table the table to search
#  @return the row and column in which letter resides, or (-1, -1) if not found
#
def getPos(letter, table):
    for row in range(len(table)):
        for col in range(len(table[row])):
            if table[row][col] == letter.upper():
                return (row, col)
    return (-1, -1)


## Create the 5x5 table for a playfair cipher.
#  @param keyword the keyword used to construct the table with no duplicates
#  @return the 5x5 encryption table
def createTable(keyword):
    # Generate an empty table.
    table = []
    for i in range(0, 5):
        table.append([0] * 5)

    # Generate all of the letters to go in the table in the correct order.
    all_letters = keyword
    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch not in all_letters:
            all_letters = all_letters + ch

    # Copy the letters into the table.
    for row in range(0, 5):
        for col in range(0, 5):
            table[row][col] = all_letters[row * 5 + col]

    # Return the result.
    return table


## Create a new version of a string containing no duplicate letters.
#  @param s the string to remove duplicate letters from
#  @return a new string where all duplicate letters have been removed
#
def removeDuplicates(s):
    retval = ""
    for ch in s:
        if ch not in retval:
            retval = retval + ch
    return retval


# Call the main function.
main()
