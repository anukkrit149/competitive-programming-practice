"""
Copyrights Reserved 
Developed By- Anukkrit Shanker
"""

def get_between_char(size,ctr):
    if ctr == 0:
        return chr(97+size-1)
    string = ''
    string += chr(97+size-1)
    for i in range(1, ctr+1):
        string += '-{}'.format(chr(97+size-1-i))
    for i in range(ctr-1, 0, -1):
        string += '-{}'.format(chr(97+size-1-i))
    string += '-{}'.format(chr(97+size-1))
    return string


def print_rangoli(size):
    width = len(get_between_char(size,size-1))
    for i in range(size-1):
        print(get_between_char(size,i).center(width, '-'))
    print(get_between_char(size,size-1))
    for i in range(size-2,-1,-1):
        print(get_between_char(size,i).center(width, '-'))


if __name__ == '__main__':
    # print(get_between_char(5,0))
    print_rangoli(5)
