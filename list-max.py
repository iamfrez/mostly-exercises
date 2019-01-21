#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'listMax' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY operations
#

def listMax(n, operations):
    # Write your code here
    alist = [0] * n
    for op in operations:
        for a in list(range(op[0]-1, op[1])):
            alist[a] += op[2]
    return max(alist)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())

    operations_rows = int(input().strip())
    operations_columns = int(input().strip())

    operations = []

    for _ in range(operations_rows):
        operations.append(list(map(int, input().rstrip().split())))

    result = listMax(n, operations)

    print(str(result) + '\n')
    #fptr.write(str(result) + '\n')
    #fptr.close()
