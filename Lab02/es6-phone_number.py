##
#  Display a phone number with nice formatting.
#

# Save the phone number in a String variable
num = '4155551212'

# Alternatively, gather input from the user.
# num = input("Enter a 10 digit phone number: ")

# Extract the parts of the number.
area_code = "(" + num[0]+num[1]+num[2] + ")"
formatted = area_code + " " + num[3]+num[4]+num[5] + "-" + num[6]+num[7]+num[8]+num[9]

# In the future, after we learn the 'slicing' operator [a:b], this may be rewritten as:
# area_code = "(" + num[0:3] + ")"
# formatted = area_code + " " + num[3:6] + "-" + num[6:]


# Display the result.
print("The formatted number is:", formatted)
