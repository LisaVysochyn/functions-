"""Write a program that asks the user to enter an input.

Print whether it is True or False
Check if an input is None or NaN and print the result of the check
>>>true_or_false(7)
True
the value is NOT None
the value is NOT NaN
"""
import math

def true_or_false(a):
    print(bool(a))
    if a == None:
        print("the value is None")
    else: print("the value is NOT None")
    if math.isnan(a) == True:
        print("the value is NaN")
    else: print("the value is NOT NaN")

#instance        
true_or_false(7) 
