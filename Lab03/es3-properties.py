##
#  Check several properties of a string.
#

# Read input from the user.
string = input("Enter a string: ")

# Check each property and display a message if that property is present.
if string.isalpha():
    print("The string contains only letters.")

elif string.isdigit():
    print("The string contains only digits.")

if string.isalpha() and string.isupper():  # v. nota
    print("All letters in the string are uppercase letters.")

elif string.isalpha() and string.islower():  # v. nota
    print("All letters in the string are lowercase letters.")

if string.isalnum():
    print("The string contains only letters and digits.")

if string[0].isupper():
    print("The string starts with an uppercase letter.")

if string.endswith("."):
    print("The string ends with a period.")

# NOTA: attenzione alle funzioni isupper/islower
# La documentazione dice:
# "Return True if all cased characters in the string are uppercase "
# "and there is at least one cased character, False otherwise"
# Quindi verifica "all CASED characters", quindi restituisce True
# se tutte le lettere sono maiuscole. I caratteri che non sono lettere
# (es. punteggiatura e spazi) non vengono controllati.
# Per questo bisogna verificare anche .isalpha(), per escludere dal
# nostro criterio dei caratteri che non siano alfabetici.
# La differenza è tra:
#   - tutti i caratteri alfabetici sono maiuscoli (.isupper())
#   - tutti i caratteri sono alfabetici maiuscoli (.isalpha() and .isupper)
