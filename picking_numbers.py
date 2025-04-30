#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    n = len(a)
    a.sort()  # Fix: added parentheses to actually sort the list
    max_count = 0

    for i in range(n):
        count = 1  # include a[i] itself
        for j in range(i + 1, n):
            if abs(a[i] - a[j]) <= 1:
                count += 1
        if count > max_count:
            max_count = count

    return max_count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
