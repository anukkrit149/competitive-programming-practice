"""
Copyrights Reserved 
Developed By- Anukkrit Shanker
"""

n = int(input().split()[0])
m = n *3

dashChar = '-'
pipeChar = '.|.'
half = int(n/2)

# upper half
for i in range(half):
        print((pipeChar*(2*i+1)).center(m,'-'))
print('WELCOME'.center(m,'-'))
# lower half
for i in range(half, 0, -1):
        print((pipeChar*(2*i-1)).center(m,'-'))



