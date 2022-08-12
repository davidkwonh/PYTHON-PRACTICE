from decimal import Decimal, getcontext

# Ints and floats


#   python will automatically put into floats when divided or using floats
a = 20 / 4
b = 5 + 3.0

#   int() is a builtin class for python
#   python breaks types into classes instead of functions
#   aka "casting"

int(3 * 5.0)

#   python throws decimal points away after
print(int(8.9))
print(int(8.99999999))

#   round class
#   (what you are rounding, what decimal place)
round(14 / 3, 2)

print(1.2 - 1.0)
#   floats are approximations and has a finite amount of memory

print(round(1.2 - 1.0, 2))

#   Int functionalities
int('100')
int('100', 2)
#   returns 4 because based 2 in string *ONLY IN STRING*

print(1.2 - 1.0)  # returns a floating point error

# DECIMAL
#   requires an import decimal at the top of the code
getcontext()
getcontext().prec = 4  # changes precision to 4
Decimal(1) / Decimal(3)

Decimal(3.14)
#   returns a long float
Decimal('3.14')

#   proves that floats gives marginal errors
print(round(1.2 - 1.0, 2))
