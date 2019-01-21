#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the braces function below.
def braces(values):
    res = []
    braces = {'{': '}', '[': ']', '(': ')'}
    for val in values:
        chain = []
        for i in val:
            if i in braces.keys():
                chain.append(i)
            else:
                if chain and braces[chain[-1]] == i:
                    chain.pop(-1)
                else:
                    #chain.append(i)
                    break
        if chain:
            res.append('NO')
        else:
            res.append('YES')
    return res

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    values_count = int(input())

    values = []

    for _ in range(values_count):
        values_item = input()
        values.append(values_item)

    res = braces(values)
    print('\n'.join(res))
    #fptr.write('\n'.join(res))
    #fptr.write('\n')

    #fptr.close()
