"""
Copyrights Reserved 
Developed By- Anukkrit Shanker
"""


def minion_game(string):
    vowels_sub = 0
    consonants_sub = 0
    n = len(string)
    for i in range(n):
        subArrLen = n-i
        if string[i] in "AEIOU":
            vowels_sub += subArrLen
        else:
            consonants_sub +=  subArrLen
    if vowels_sub < consonants_sub:
        print('Stuart {}'.format(consonants_sub))
    elif vowels_sub== consonants_sub:
        print('Draw')
    else:
        print('Kevin {}'.format(vowels_sub))





if __name__ == '__main__':
    s = input()
    minion_game(s)