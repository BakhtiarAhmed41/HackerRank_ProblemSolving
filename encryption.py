#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    s = s.replace(" ", "")
    n = len(s)
    rows = int(math.floor(math.sqrt(n)))
    cols = int(math.ceil(math.sqrt(n)))

    if rows * cols < n:
        rows = cols

    encoded = [['' for _ in range(cols)] for _ in range(rows)]
    
    k = 0
    for i in range(rows):
        for j in range(cols):
            if k < n:
                encoded[i][j] = s[k]
                k += 1
        
    result = ""
    for i in range(cols):
        for j in range(rows):
            if encoded[j][i]:  # Avoid appending empty values
                result += encoded[j][i]
        result += " "
        
    return result.strip()

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
