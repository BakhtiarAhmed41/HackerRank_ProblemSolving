#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    factorial = 1
    
    if n == 0:
        print(factorial)
    else:
        for i in range(n):
            factorial = factorial * (n-i)
        
        print(factorial)
        
        
if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)
