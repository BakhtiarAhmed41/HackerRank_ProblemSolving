#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    
    no_apples = []
    number_of_apples  = 0
    no_oranges = []
    number_of_oranges  = 0
    
    for i in range(len(apples)):
        no_apples.append(apples[i] + a)

    for i in range(len(oranges)):
        no_oranges.append(oranges[i] + b) 

    for i in range(len(no_apples)):
        if((no_apples[i]>=s) and (no_apples[i]<= t)):
            number_of_apples +=1   
        else: 
            continue
    
    for i in range(len(no_oranges)):
        if((no_oranges[i]>=s) and (no_oranges[i]<= t)):
            number_of_oranges +=1   
        else: 
            continue

    print(number_of_apples)
    print(number_of_oranges)
    
    
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
