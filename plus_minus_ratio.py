#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos_numbers = 0
    neg_numbers = 0
    zeros = 0
    
    for i in range(n):
        
        if arr[i]>0:
            pos_numbers +=1
        elif arr[i]<0:
            neg_numbers +=1
        else:
            zeros +=1

    print(f"{pos_numbers/n:.6f}")
    print(f"{neg_numbers/n:.6f}")
    print(f"{zeros/n:.6f}")

    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
