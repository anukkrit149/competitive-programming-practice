"""
Copyrights Reserved 
Developed By- Anukkrit Shanker
"""


def reverse(a):
    l_ptr = 0
    r_ptr = len(a)-1
    while l_ptr<r_ptr:
        a[l_ptr],a[r_ptr] = a[r_ptr],a[l_ptr]
        l_ptr +=1
        r_ptr -=1



a = ['A', 'B', 'C', 'D', 'E']

reverse(a)

print(a)