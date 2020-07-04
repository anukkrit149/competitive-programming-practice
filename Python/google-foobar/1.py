"""
Copyrights Reserved 
Developed By- Anukkrit Shanker
"""


def solution(x, y):
    x = list(set(x))
    y = list(set(y))
    n1 = len(x)
    n2 = len(y)

    max_len = max(n1, n2)
    const = 0
    for i in range(max_len):
        if i < n1:
            if not x[i] in y:
                const = x[i]
                break
        if i < n2:
            if not y[i] in x:
                const = y[i]
                break
    return const


print(solution([13,5,6,2,5],[5,2,5,13]))