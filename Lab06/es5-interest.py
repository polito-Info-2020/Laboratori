##
#  Compute the future value of an investment.
#

def main():
    print("In 3 years at 4%%, $10000 will be %.2f" % futureValue(10000, 4, 3))
    print("In 4 years at 3.5%%, $5000 will be %.2f" % futureValue(5000, 3.5, 4))
    print("In 1 year at 10%%, $1000 will be %.2f" % futureValue(1000, 10, 1))


## Compute the future value of an investment.
#  @param init the initial value of the investment
#  @param rate the interest rate in percent
#  @param years the number of years
#  @return the future value of the investment
#
def futureValue(init, rate, years):
    return init * (1 + rate / 100) ** years


# Call the main function.
main()
