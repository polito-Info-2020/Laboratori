##
#  Convert a numeric grade to the closest letter grade.
#

# Read input from the user.
num = float(input("Enter a numeric grade: "))

# find the letter
closestInteger = round(num,0)
if closestInteger == 4:
    letter = 'A'
elif closestInteger == 3:
    letter = 'B'
elif closestInteger == 2:
    letter = 'C'
elif closestInteger == 1:
    letter = 'D'
else:
    letter = 'F'

if letter != 'F':
    delta = num-closestInteger
    if delta >= 0.3:
        letter = letter + '+'
    elif delta <= -0.3:
        letter = letter + '-'

# Display the result.
print("The letter grade is %s." % letter)
