#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.


def findDigits(n):
    
    number = str(n)
    count = 0
    
    for i in range(len(number)):
        
        if(int(number[i])==0):
            continue
        
        elif(n%int(number[i])==0):
            count += 1
        
        else:
            continue
    
    return count    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
