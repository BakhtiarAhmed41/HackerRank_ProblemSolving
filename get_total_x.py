#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    
    num = 0
    number = False
    for i in range(max(a), min(b)+1):
        
        for j in range(n):
            
            if(j == n-1):
                if(i%a[j]==0):
                    number = True
                    break
            else:
                if(i%a[j]==0):
                    continue
                else:
                    break
        
        if(number):
            for j in range(m):
            
                if(j == m-1):
                    if(b[j]%i==0):
                        num += 1
                        break
                else:
                    if(b[j]%i==0):
                        continue
                    else:
                        break
        number = False       
    return num
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
