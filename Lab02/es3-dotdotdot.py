##
#  Print the first 3 letters of a string, followed by ..., followed by the 
#  last 3 letters of a string.
#

# Initialize the string.
string = "Mississippi"

# Length of the String
lenString = len(string) 

# Display the result.
print(string[0]+string[1]+string[2]+'...'+string[lenString-3]+string[lenString-2]+string[lenString-1])
# Alternatively
print("%s%s%s...%s%s%s" % (string[0], string[1], string[2], string[lenString-3], string[lenString-2], string[lenString-1]))
