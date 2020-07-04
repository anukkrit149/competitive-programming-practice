"""
Copyrights Reserved 
Developed By- Anukkrit Shanker
"""

nTest = int(input())
testArr = list()

for i in range(nTest):
    nInputs = int(input())
    testArr.append(list(map(int, input().split())))
social_dist = list()

for i in range(nTest):
    lenTestCase = len(testArr[i])
    temp_list = list()
    temp_list.append(testArr[i][0])
    for j in range(1, lenTestCase):
        temp_list.append(testArr[i][j] - testArr[i][j - 1])
    social_dist.append(temp_list)
res = list()

for i in range(nTest):
    min_pat = 0
    max_pat = 0