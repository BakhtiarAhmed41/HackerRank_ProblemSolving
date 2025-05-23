#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def utopianTree(n):
    height = 0
    if(n==0):
        height = 1
    else:
        for i in range(n+1):
            
            if(i==0):
                height =1
            
            elif i ==1:
                height = height*2
                
            elif i % 2 !=0:
                height = height * 2
                
            else:
                height += 1
    
    return height        
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
