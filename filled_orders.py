#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the 'filledOrders' function below.

# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY order
#  2. INTEGER k


def filledOrders(order, k):
    orders = 0
    for i in range(0, len(order)):
        order.sort()
        if order[i]<= k:
            orders += 1
            k = k-order[i]
        else:
            break
    
    return orders
        
        
