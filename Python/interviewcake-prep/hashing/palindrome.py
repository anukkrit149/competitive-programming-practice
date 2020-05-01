"""
Copyrights Reserved 
Developed By- Anukkrit Shanker
"""

def has_palindrome_permutation(the_string):
    # the_string = list(the_string)
    chars_dict = dict()
    for i in the_string:
        if chars_dict.get(i) is not None:
            chars_dict[i] += 1
        else:
            chars_dict.setdefault(i,1)
    flagOdd = 1
    for i in chars_dict.values():
        if i%2 != 0:
            flagOdd -= 1
        if flagOdd < 0:
            return False
    return True



print(has_palindrome_permutation('aabcbcd'))


# solution

# def has_palindrome_permutation(the_string):
#     # Track characters we've seen an odd number of times
#     unpaired_characters = set()
#
#     for char in the_string:
#         if char in unpaired_characters:
#             unpaired_characters.remove(char)
#         else:
#             unpaired_characters.add(char)
#
#     # The string has a palindrome permutation if it
#     # has one or zero characters without a pair
#     return len(unpaired_characters) <= 1