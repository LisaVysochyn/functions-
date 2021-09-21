"""Function to sort hte tuple  by second item of tuple

>>>(('rishav', 10), ('akash', 5), ('ram', 20), ('gaurav', 15))
(('akash', 5), ('rishav', 10), ('gaurav', 15), ('ram', 20))
"""
def sortby2(tup_of_tups):
    return tuple(sorted(tup_of_tups, key = lambda x: x[1]))

#example
tup = (('rishav', 10), ('akash', 5), ('ram', 20), ('gaurav', 15))
print(sortby2(tup)) 
