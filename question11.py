"""a funtion that return reversed tuple

>>>rev_tupl((1, 5, 6, 0, 8))
(8, 0, 6, 5, 1)
"""
def rev_tupl(tuples):
    return tuples[::-1]

#example
print(rev_tupl((1, 5, 6, 0, 8)))
