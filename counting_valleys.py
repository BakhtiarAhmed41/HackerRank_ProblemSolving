#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    arr = list(path)
    valleys = 0
    count = 0
    for i in range(steps):
        if arr[i] == 'U':
            count+=1
            if(count == 0):
                valleys +=1
                
        elif arr[i] == 'D':
            count-=1

    return valleys
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
