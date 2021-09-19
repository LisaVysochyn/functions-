'''Write a program that asks the user how many credits they have taken.
If they have taken 23 or less, print that the student is a freshman.
If they have taken between 24 and 53, print that they are a sophomore.
The range for juniors is 54 to 83, and for seniors it is 84 and over.'''

credits = int(input('Enter your credits: '))

if credits<0:
    print('The entry is invalid!')
if credits>=0 and credits<=23:
    print('The student is a freshman.')
if credits>=24 and credits<=53:
    print('The student is a sophomore.')
if credits>=54 and credits<=83:
    print('The student is a junior.')
if credits>=84 and credits<=100:
    print('The student is a senior.')
