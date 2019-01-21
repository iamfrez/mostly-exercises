#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'reformatDate' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY dates as parameter.
#

def reformatDate(dates):
    # Write your code here
    import datetime as dt
    date_format = '%Y-%m-%d'
    res = []
    months = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7,'Aug': 8,'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
    for date in dates:
        day, month, year = date.split(' ')
        day = int(day[0:-2])
        year = int(year)
        month = int(months[month])
        d = dt.date(year, month, day)
        res.append(d.strftime(date_format))
    return res

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    dates_count = int(input().strip())

    dates = []

    for _ in range(dates_count):
        dates_item = input()
        dates.append(dates_item)

    result = reformatDate(dates)

    print('\n'.join(result))
    #fptr.write('\n'.join(result))
    #fptr.write('\n')

    #fptr.close()

