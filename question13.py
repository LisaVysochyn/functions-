"""a function that removes empty strings from the list of strings.
>>>["a", "", "c"]
['a', 'c']
"""
def del_empy(l):
    return [string for string in l if string != ""]
#instane
a_list = ["a", "", "c"]
print(del_empy(a_list))
