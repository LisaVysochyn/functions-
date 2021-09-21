"""A function called sumDigits that for a given 4-digit
integer num returns its sum of the digits.

>>>sumDigits(1234)
10
"""

def sumDigits(integer):
    l_integer = [int(a) for a in str(integer)]
    if len(l_integer) == 4:
        return sum(l_integer)
    else: print("Error: please enter 4-digit integer")
    
#instance
print(sumDigits(1234))
