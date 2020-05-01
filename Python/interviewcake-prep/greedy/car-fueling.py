"""
Copyrights Reserved 
Developed By- Anukkrit Shanker
"""


def min_fuels(X,n,L):
    ctr = 0
    current_stop = X[0]
    stops = list()
    for i in range(len(X)-1):
        if (X[i]-current_stop) < L and not (X[i+1]-current_stop) < L :
            current_stop = X[i]
            stops.append(X[i])
            ctr += 1
        elif (X[i]-current_stop) > L:
            return "Impossible"

    return ctr


print(min_fuels([0,220,340,500,600],3,300))