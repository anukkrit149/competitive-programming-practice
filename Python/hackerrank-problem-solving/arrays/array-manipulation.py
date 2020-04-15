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


# Naives approach time limit exceed
# def arrayManipulation(n, queries):
#     zeroes_arr = [0]*(n+1)
#     # print(zeroes_arr)
#     for query in queries:
#         a, b, k = query
#         for i in range(a, b + 1):
#             zeroes_arr[i] += k
#     return max(zeroes_arr)

# Naives approach time limit exceed
def arrayManipulation(n, queries):
    zeroes_arr = [0]*(n+1)
    for i in range(len(queries)):
        a, b, k = queries[i]
        zeroes_arr[a-1] += k
        if b < len(zeroes_arr):
            zeroes_arr[b] -= k
    print(zeroes_arr)
    val = 0
    maximum = 0
    for i in zeroes_arr:
        val += i
        if maximum<val:
            maximum = val
    return maximum







# numpy implementation working
# def arrayManipulation(n, queries):
#     zeroes_arr = np.zeros(n)
#     for query in queries:
#         zeroes_arr[query[0]-1:query[1]-1] += query[2]
#     return int(max(zeroes_arr))


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)
    print(n)

    print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
