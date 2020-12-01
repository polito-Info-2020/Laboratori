##
#  Compute and display the total price of a book order.
#

# Define constants.
TAX_RATE = 0.075
SHIPPING_PER_BOOK = 2.0

# Save the price of the books and the number of books in two constant variables
BOOK_PRICE = 53.0
NUM_BOOKS = 15

# Alternatively, gather input from the user.
# bookPrice = float(input("Enter the total book price: "))
# numBooks = int(input("Enter the number of books: "))

# Compute the total price.
tax = BOOK_PRICE * TAX_RATE
shipping = NUM_BOOKS * SHIPPING_PER_BOOK
total_price = BOOK_PRICE + tax + shipping

# Display the result.
print("The total cost of the order is $%.2f." % total_price)
