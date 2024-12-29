#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    min = 0
    max = 0
    arr.sort()
    for i in range(0,4):
        min += arr[i]
        
    for i in range(1,5):
        max += arr[i]
        
    print(min,end=" ")
    print(max)
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
