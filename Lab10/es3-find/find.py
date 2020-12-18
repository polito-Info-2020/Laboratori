##
#  Find occurrences of a word in several files.
#
import sys

# Extract the target from the command line.
target = input('Insert the word to search: ')

filenames = input('Insert the list of files to search (separate with ,): ')
# For each filename on the command line.
for filename in filenames.split(','):
    # Save the filename and open the file.
    inf = open(filename.strip(), "r")

    # Search each line in the file for the target.
    for line in inf:
        if target in line:
            print("%s: %s" % (filename, line), end="")

    # Close the file.
    inf.close()
