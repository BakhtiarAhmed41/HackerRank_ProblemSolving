#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    time = s[:-2].split(':')
    period = s[-2:]
    
    if period == "AM":
        if time[0] == "12":
            time[0] = "00"
    else:
        if time[0] != "12":
            time[0] = str(int(time[0]) + 12)
    
    return ':'.join(time)

                
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
