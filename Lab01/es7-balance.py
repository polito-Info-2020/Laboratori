##
#  Compute the balance of an account with an initial balance of $1,000
#  with an annual interest rate of 5% after 1, 2 and 3 years.
#
balance = 1000
rate = 0.05 # 5/100

#  The balance after year one.
balance = balance + balance * rate
print("After year 1, the balance is", balance)

#  The balance after year two.
balance = balance + balance * rate
print("After year 2, the balance is", balance)

#  The balance after year three.
balance = balance + balance * rate
print("After year 3, the balance is", balance)

