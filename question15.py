"""a function called is_sorted that is given a list
and returns True if the list is sorted and False otherwise.

>>>is_sorted(["a", "b"]
True
"""

def is_sorted(a):
    return a == sorted(a)
print(is_sorted(["a", "c"]))
