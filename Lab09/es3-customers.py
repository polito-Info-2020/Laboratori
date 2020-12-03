##
#  Display the best customer of the day.
#
def main() :
   sales = []
   names = []

   # Read the names and sales amounts, storing them in two lists.
   amount = float(input("Enter the sale amount: "))
   while amount != 0 :
      sales.append(amount)

      name = input("Enter the customer's name: ")
      names.append(name)

      amount = float(input("Enter the sale amount: "))

   # Compute and display the name of the best customer.
   bestName = nameOfBestCustomer(sales, names)
   print("The best customer was:", bestName)


## Identify the name of the best customer.
#  @param sales the list of sale amounts
#  @param customers the names of the customers
#  @return the name of the customer with the highest sale amount
#
def nameOfBestCustomer(sales, customers) :
   # Find the largest sale.
   largest = max(sales)

   # Display the name of the best customer.
   for i in range(0, len(sales)) :
      if sales[i] == largest :
         return customers[i]

# Call the main function.
main()

