#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    arr.sort()
    type = {arr[0] : arr.count(arr[0])}
    
    
    for i in range(1, len(arr)):
        if(arr[i] == arr[i-1]):
            continue
        else:
            type[arr[i]] = arr.count(arr[i])
    
    return max(type, key=type.get)
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
