##
#  Convert a numeric grade to the closest letter grade.
#

# Read input from the user.
num = float(input("Enter a numeric grade: "))

# Convert to a letter grade.
if num >= 3.85:
    letter = "A"
elif num >= 3.5:
    letter = "A-"
elif num >= 3.15:
    letter = "B+"
elif num >= 2.85:
    letter = "B"
elif num >= 2.5:
    letter = "B-"
elif num >= 2.15:
    letter = "C+"
elif num >= 1.85:
    letter = "C"
elif num >= 1.5:
    letter = "C-"
elif num >= 1.15:
    letter = "D+"
elif num >= 0.85:
    letter = "D"
elif num >= 0.5:
    letter = "D-"
else:
    letter = "F"

# Display the result.
print("The letter grade is %s." % letter)
