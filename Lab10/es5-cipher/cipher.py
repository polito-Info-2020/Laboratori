##
#  Implement a random monoalphabet cipher.
#

def main():
    keyword = input('Insert the keyword: ')
    keyword = removeDuplicates(keyword)
    keyword = keyword.upper()

    # Extract the filenames from the command line and open them.
    input_name = input('Input file name: ')
    inf = open(input_name, "r")

    output_name = input('Output file name: ')
    outf = open(output_name, "w")

    # Construct the full key string with the remaining letters of the
    # alphabet appended in reverse order.
    key_string = keyword
    for ch in "ZYXWVUTSRQPONMLKJIHGFEDCBA":
        if ch not in key_string:
            key_string = key_string + ch

    action = input('Do you want to encrypt or decrypt (e/d)? ')

    # Encrypt the file.
    if action == 'e':
        for line in inf:
            for ch in line:
                pos = -1
                if "A" <= ch <= "Z":
                    pos = ord(ch) - ord("A")
                    outf.write(key_string[pos])
                elif "a" <= ch <= "z":
                    pos = ord(ch) - ord("a")
                    outf.write(key_string[pos].lower())
                else:
                    outf.write(ch)
    # Decrypt the file.
    elif action == 'd':
        for line in inf:
            for ch in line:
                out_ch = ch
                if ch in key_string:
                    out_ch = chr(ord("A") + key_string.index(ch))
                elif ch in key_string.lower():
                    out_ch = chr(ord("a") + key_string.lower().index(ch))
                outf.write(out_ch)
    # Handle the case where the user failed to specify the operation.
    else:
        exit("Either d or e must be provided for decrypt or encrypt.")

    # Close the files.
    inf.close()
    outf.close()


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
