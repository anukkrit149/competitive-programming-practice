#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    res_values = dict()
    for i in range(len(queries)):
        res_values[i] = 0
    # print(res_values)
    for query in set(queries):
        count = strings.count(query)
        indices_for_query = list()
        for i in range(len(queries)):
            if query == queries[i]:
                indices_for_query.append(i)
        for i in indices_for_query:
            res_values[i] = count

    return list(res_values.values())


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)
    print(res)

    # fptr.write('\n'.join(map(str, res)))
    # fptr.write('\n')

    # fptr.close()
