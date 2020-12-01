##
#  Read three strings and sort them lexicographically.
#

# Read input from the user.
str1 = input("Enter a string: ")
str2 = input("Enter a string: ")
str3 = input("Enter a string: ")

# Order the strings so that first comes before second, which comes before 
# third.
if str1 <= str2 and str1 <= str3:
    first = str1
    if str2 <= str3:
        second = str2
        third = str3
    else:
        second = str3
        third = str2
elif str2 <= str1 and str2 <= str3:
    first = str2
    if str1 <= str3:
        second = str1
        third = str3
    else:
        second = str3
        third = str1
else:
    first = str3
    if str2 <= str1:
        second = str2
        third = str1
    else:
        second = str1
        third = str2

# Display the result.
print(first)
print(second)
print(third)
