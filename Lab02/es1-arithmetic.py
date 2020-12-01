##
#  Save two integers in two constants, and display the result of several
#  calculations involving them.
#

NUM_1 = 20
NUM_2 = 40

# Alternatively, read the integers from the user.
# NUM_1 = int(input("Enter an integer: "))
# NUM_2 = int(input("Enter another integer: "))

# Compute and display the sum, difference, product, average, distance, 
# minimum and maximum.
print("Sum:", NUM_1 + NUM_2)
print("Difference:", NUM_1 - NUM_2)
print("Product:", NUM_1 * NUM_2)
print("Average:", (NUM_1 + NUM_2) / 2)
print("Distance:", abs(NUM_1 - NUM_2))
print("Minimum:", min(NUM_1, NUM_2))
print("Maximum:", max(NUM_1, NUM_2))
