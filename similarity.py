#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'usernameDisparity' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY inputs as parameter.
#

def suffixes(word):
    s = []
    for i in range(1, len(word)):
        s.append(word[i:])
    return s

def usernameDisparity(inputs):
    # Write your code here:
    result = []
    for word in inputs:
        suffixes = []
        nums = []
        [suffixes.append(word[i:]) for i in range(1, len(word))]
        for s in suffixes:
            similarity = 0
            for a, b in zip(word, s):
                if a == b:
                    similarity += 1
            nums.append(similarity)
        nums.append(len(word))
        result.append(sum(nums))
    return result


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    inputs_count = int(input().strip())

    inputs = []

    for _ in range(inputs_count):
        inputs_item = input()
        inputs.append(inputs_item)

    result = usernameDisparity(inputs)

    print('\n'.join(map(str, result)))
    #fptr.write('\n'.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()

