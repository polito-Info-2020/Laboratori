##
#  Read a file and save it to a new file with line numbers.
#

# Read the file names from the user.
inputName = input("Enter the input file name: ")
outputName = input("Enter the output file name: ")

# Open the input and output file names.
inf = open(inputName, "r")
outf = open(outputName, "w")

# Read lines from the file and save them to a new file with line numbers.
number = 1
for line in inf:
    outf.write("/* " + str(number) + " */ " + line)
    number = number + 1

# Close the files.
inf.close()
outf.close()
