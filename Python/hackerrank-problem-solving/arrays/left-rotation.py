# !/bin/python3

import math
import os
import random
import re
import sys


def left_rotations(n, d, a):
    for _ in range(d):
        a.insert(n-1,a.pop(0))
    return a



if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))


    print(*left_rotations(n, d, a))
    # for i in left_rotations(n, d, a):
    #     print(i)
