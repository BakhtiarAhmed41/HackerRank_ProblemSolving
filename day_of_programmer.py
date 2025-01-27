#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    
    
    
    if(year<1918):
        if(year%4==0):
            y = f"12.09.{year}"
            return y
        else:
            y = f"13.09.{year}"
            return y
    
    elif(year==1918):
        y = f"26.09.{year}"
        return y
            
    else:    
        if((year%400==0) or (year%4==0 and year%100!=0)):
            y = f"12.09.{year}"
            return y
        
        else:
            y = f"13.09.{year}"
            return y

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
