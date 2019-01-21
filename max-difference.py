#!/bin/python3
import math
import os
import random
import re
import sys
# Complete the maxDifference function below.
def maxDifference(a):
    max_diff = -1
    i = 0
    while i < len(a) - 1:
        j = i + 1
        while j < len(a):
            res = a[j] - a[i]
            if res > max_diff:
                max_diff = res
            j += 1
        i += 1
    return max_diff

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    a_count = int(input())
    a = []
    for _ in range(a_count):
        a_item = int(input())
        a.append(a_item)
    res = maxDifference(a)
    print('\n' + str(res) + '\n')
    #fptr.write(str(res) + '\n'i)
    #fptr.close()
