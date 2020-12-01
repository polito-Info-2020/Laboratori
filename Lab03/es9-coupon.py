##
#  Compute a coupon amount based on the amount spent.
#

# Read input from the user.
cost = float(input("Please enter the cost of your groceries: "))

# Compute the discount coupon amount.
if cost < 10:
    factor = 0
elif cost < 60:
    factor = 8
elif cost < 150:
    factor = 10
elif cost < 210:
    factor = 12
else:
    factor = 14

coupon = cost * factor / 100

# Display the result.
print("You win a discount coupon of $%.2f. (%d%% of your purchase)" %
      (coupon, factor))
