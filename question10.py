""" Function accept 6 arguents(date, month, year) of two dates and calculate
number of business days between
two dates using datetime module.

>>>busdays(20, 4, 1999, 20, 5 , 1999)
23
"""

import datetime

def busdays(d1, m1, y1, d2, m2, y2):
    date1, date2 =  datetime.date(y1, m1, d1), datetime.date(y2, m2, d2)
    all_dates = [(date1 + datetime.timedelta(days=i)) for i in range((date2-date1).days + 1)]
    return len([i for i in all_dates if i.weekday() < 5])

#example
print(busdays(20, 4, 1999, 20, 5 , 1999))
