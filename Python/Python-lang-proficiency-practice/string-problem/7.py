"""
Copyrights Reserved 
Developed By- Anukkrit Shanker
"""

import textwrap


def merge_the_tools(string, k):

    subSegments = textwrap.wrap(string, k)
    for i in range(len(subSegments)):
        removeRedundancy = dict()
        print(''.join([removeRedundancy.setdefault(i,i) for i in subSegments[i] if i not in removeRedundancy]))



if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)