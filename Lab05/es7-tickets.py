##
#  Sell a limited number of cinema tickets.
#

# Define constant variables.
LIMIT = 100

# Count the number of buyers until all of the tickets are sold.
num_buyers = 0
tickets = LIMIT
while tickets > 0:
    print("There are currently", tickets, "tickets remaining.")

    # Get the number of tickets that want to be purchased in the current
    # transaction, ensuring that the number of tickets is legal.
    current = int(input("How many tickets would you like to purchase? "))
    while current > 4 or current > tickets or current < 1:
        print("Sorry, you can't buy that many.")
        current = int(input("How many tickets would you like to purchase? "))

    tickets = tickets - current
    num_buyers = num_buyers + 1

# Display the number of buyers.
print("The total number of buyers was", num_buyers)
