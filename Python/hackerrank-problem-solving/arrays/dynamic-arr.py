#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    last_ans = 0
    res = dict()
    ans = list()
    for i in range(n):
        res[i] = list()
    for query in queries:
        print(query)
        x = int(query[1])
        y = int(query[2])
        idx = ((x ^ last_ans) % n)
        if query[0] == 1:
            print("query1")
            res[idx].append(y)
        else:
            print("query2")
            print(idx)
            print(res[idx])
            last_ans = res[idx][y % len(res[idx])]
            ans.append(last_ans)
            print(last_ans)
        print(res)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
