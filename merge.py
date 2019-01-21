import math
import os
import random
import re
import sys



#
# Complete the 'mergeArrays' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def mergeArrays(a, b):
    # Write your code here
    #print(a)
    #print(b)
    #c = []
    #is_sorted = False
    return sorted(a + b)


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    b_count = int(input().strip())

    b = []

    for _ in range(b_count):
        b_item = int(input().strip())
        b.append(b_item)

    result = mergeArrays(a, b)

    print('\n'.join(map(str, result)))
    #fptr.write('\n'.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()

