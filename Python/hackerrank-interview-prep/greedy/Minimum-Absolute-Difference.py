"""
Copyrights Reserved 
Developed By- Anukkrit Shanker
"""

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    arr = sorted(arr)
    dif = set()
    for i in range(len(arr)-1):
        dif.add(abs(arr[i]-arr[i+1]))
    return min(dif)



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
