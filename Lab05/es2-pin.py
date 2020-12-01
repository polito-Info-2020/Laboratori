##
#  Simulate a bank machine validating a user's PIN.
#
from sys import exit

# Define constants.
CORRECT_PIN = "1234"

# Number of attempts
attempts = 3
# Boolean variable to represent whether the PIN is correct or not
pinIsCorrect = False

while attempts > 0 and not pinIsCorrect:
    pin = input("Enter your PIN: ")

    if pin == CORRECT_PIN:
        pinIsCorrect = True
        print("Your PIN is correct")

    attempts = attempts - 1

if not pinIsCorrect:
    print("Your bank card is blocked")

# Alternative solution without using a cicle (erase line 28 and 52 to uncomment)

'''
# Read the PIN for the first time.
pin = input("Enter your PIN: ")

if pin == CORRECT_PIN :
   exit("Your PIN is correct")

print("Your PIN is incorrect")

# Read the PIN for the second time.
pin = input("Enter your PIN: ")

if pin == CORRECT_PIN :
   exit("Your PIN is correct")

print("Your PIN is incorrect")

# Read the PIN for the third time.
pin = input("Enter your PIN: ")

if pin == CORRECT_PIN :
   exit("Your PIN is correct")

print("Your bank card is blocked")
'''
