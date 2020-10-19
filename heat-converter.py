####################
## Heat Converter ## 
## By YV31        ##
####################

import sys
import decimal
from decimal import Decimal, getcontext

getcontext().rounding = decimal.ROUND_DOWN

argv = sys.argv[1:]
arg1, arg2, value = None, None, None


""" Heat types """

# Celsius
class Celsius:
    def __init__(self, value):
        self.value = Decimal(value)

    def to_fahrenheit(self):
        return (self.value * Decimal(1.8)) + Decimal(32)

    def to_kelvin(self):
        return self.value + Decimal(273.15)

# Kelvin
class Kelvin:
    def __init__(self, value):
        self.value = Decimal(value)

    def to_celsius(self):
        return self.value - Decimal(273.15)

    def to_fahrenheit(self):
        return ((self.value - Decimal(273.15)) * Decimal(1.8)) + Decimal(32)

# Fahrenheit
class Fahrenheit:
    def __init__(self, value):
        self.value = Decimal(value)

    def to_celsius(self):
        return (self.value / Decimal(1.8)) - Decimal(32)

    def to_kelvin(self):
        return ((self.value - Decimal(32)) / Decimal(1.8)) - Decimal(273.15)


""" Getting arguments """

# Getting input type argument.
if not argv:
    sys.exit("\033[31mERROR\033[0m: no argument.\nTry the command --help or -h to get some help.")
elif argv[0] == "-h" or argv[0] == "--help":
    sys.exit("""
Usage:
    python3 heat-converter.py <input-type> <output-type> <input-value>

Options:
    -h, --help                                           to get help.
    -c, --celsius                               input or output type.
    -k, --kelvin                                input or output type.
    -f, --fahrenheit                            input or output type.
    """)

elif argv[0] == "-c" or argv[0] == "--celsius":
    arg1 = "c"
elif argv[0] == "-k" or argv[0] == "--kelvin":
    arg1 = "k"
elif argv[0] == "-f" or argv[0] == "--fahrenheit":
    arg1 = "f"
else:
    sys.exit("\033[31mERROR\033[0m: invalid argument.\nTry the command --help or -h to get some help.")


# Getting output type argument.
if not argv[1:]:
    sys.exit("\033[31mERROR\033[0m: no second argument.\nTry the command --help or -h to get some help.")
elif argv[1] == "-c" or argv[1] == "--celsius":
    arg2 = "c"
elif argv[1] == "-k" or argv[1] == "--kelvin":
    arg2 = "k"
elif argv[1] == "-f" or argv[1] == "--fahrenheit":
    arg2 = "f"
else:
    sys.exit("\033[31mERROR\033[0m: invalid second argument.\nTry the command --help or -h to get some help.")


# Getting value argument.
if not argv[2:]:
    sys.exit("\033[31mERROR\033[0m: no value to convert.\nTry the command --help or -h to get some help.")
elif argv[3:]:
    sys.exit("\033[31mERROR\033[0m: Too many arguments.\nTry the command --help or -h to get some help.")

try:
    value = Decimal(argv[2])
except Exception as arr:
    sys.exit(f"\033[31mERROR\033[0m: Invalid input value.\nTry the command --help or -h to get some help.")


""" Returning the result """

# Returning celsius convertion.
if arg1 == "c" and arg2 == "c":
    print(f"\nCelsius: {value}")
elif arg1 == "c" and arg2 == "k":
    print(f"\nKelvin: {Celsius(value).to_kelvin()}")
elif arg1 == "c" and arg2 == "f":
    print(f"\nFahrenheit: {Celsius(value).to_fahrenheit()}")


# Returning kelvin convertion.
if arg1 == "k" and arg2 == "c":
    print(f"\nCelsius: {Kelvin(value).to_celsius()}")
elif arg1 == "k" and arg2 == "k":
    print(f"\nKelvin: {value}")
elif arg1 == "k" and arg2 == "f":
    print(f"\nFahrenheit: {Kelvin(value).to_fahrenheit()}")


# Returning fahrenheit convertion.
if arg1 == "f" and arg2 == "c":
    print(f"\nCelsius: {Fahrenheit(value).to_celsius()}")
elif arg1 == "f" and arg2 == "k":
    print(f"\nKelvin: {Fahrenheit(value).to_kelvin()}")
elif arg1 == "f" and arg2 == "f":
    print(f"\nFahrenheit: {value}")
