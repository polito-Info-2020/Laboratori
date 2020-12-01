##
#  Perform unit conversions, rejecting incompatible units.
#
from sys import exit

# Read the unit to convert from and to.

fromUnit = input("Convert from? (ml, l, g, kg, mm, cm, m, km): ")
toUnit = input("Convert to? (fl. oz, gal, oz, lb, in, ft, mi): ")

# Volume units.
if fromUnit == "ml" and toUnit == "fl. oz":
    factor = 0.03381406
elif fromUnit == "l" and toUnit == "fl. oz":
    factor = 33.81405650
elif fromUnit == "ml" and toUnit == "gal":
    factor = 0.00026417
elif fromUnit == "l" and toUnit == "gal":
    factor = 0.26417218

# Weight / mass units.
elif fromUnit == "g" and toUnit == "oz":
    factor = 0.03527399
elif fromUnit == "kg" and toUnit == "oz":
    factor = 35.27399072
elif fromUnit == "g" and toUnit == "lb":
    factor = 0.00220462
elif fromUnit == "kg" and toUnit == "lb":
    factor = 2.20462442

# Distance units.
elif fromUnit == "mm" and toUnit == "in":
    factor = 0.03937008
elif fromUnit == "cm" and toUnit == "in":
    factor = 0.39370079
elif fromUnit == "m" and toUnit == "in":
    factor = 39.37007874
elif fromUnit == "km" and toUnit == "in":
    factor = 39370.07874016
elif fromUnit == "mm" and toUnit == "ft":
    factor = 0.00328084
elif fromUnit == "cm" and toUnit == "ft":
    factor = 0.03280840
elif fromUnit == "m" and toUnit == "ft":
    factor = 3.28083990
elif fromUnit == "km" and toUnit == "ft":
    factor = 3280.83989501
elif fromUnit == "mm" and toUnit == "mi":
    factor = 0.00000062
elif fromUnit == "cm" and toUnit == "mi":
    factor = 0.00000621
elif fromUnit == "m" and toUnit == "mi":
    factor = 0.00062137
elif fromUnit == "km" and toUnit == "mi":
    factor = 0.62137119

# Incompatible units.
else:
    exit("Those units are not compatible.")

# Read the value to convert from the user.
value = float(input("Value? "))

# Compute the result.
result = value * factor

# Display the result.
print(value, fromUnit, "=", result, toUnit)
