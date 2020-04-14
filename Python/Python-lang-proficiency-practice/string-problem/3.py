"""
Copyrights Reserved
Developed By- Anukkrit Shanker
"""

n = int(input())
def binary_num(n):
    bin_n = ''
    while n >= 1:
        rem = int(n % 2)
        bin_n += str(rem)
        n /= 2
    return bin_n[::-1]

def octal_num(n):
    rem_str = ''
    while n >= 1:
        rem_str += str(int(n % 8))
        n /= 8
    return rem_str[::-1]

def hexadecimal_num(n):
    rem_str = ''
    characters = {
        10:'A',
        11:'B',
        12:'C',
        13:'D',
        14:'E',
        15:'F'
    }
    while n >= 1:
        rem = int(n%16)
        n /= 16
        if rem < 10:
            rem_str += str(rem)
        else:
            rem_str += characters[rem]
    return rem_str[::-1]

for i in range(n+1):
    print(str(i)+'\t'+str(octal_num(i))+'\t'+str(hexadecimal_num(i))+'\t'+str(binary_num(i))+'\n')