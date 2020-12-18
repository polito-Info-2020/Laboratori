##
#  Generate a grade report for a student.
#

# Read the student id from the user.
sid = input("Enter the student id: ")

# Process each class found in classes.txt.
courses = open("classes.txt", "r")
print("Student ID", sid)
for course in courses:
    # Remove the trailing newline from the class number.
    course = course.rstrip()

    # Open the list for the class and search for the student.
    inf = open(course + ".txt", "r")
    for line in inf:
        parts = line.split()
        # If the student is in the class then print the mark.
        if sid == parts[0]:
            print(course+' '+line, end="")

    # Close the class file.
    inf.close()

# Close the list of classes.
courses.close()
