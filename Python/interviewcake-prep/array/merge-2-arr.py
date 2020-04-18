"""
Copyrights Reserved 
Developed By- Anukkrit Shanker
"""

my_list = [3, 4, 6, 10]
alices_list = [1, 5, 8, 12]


# Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
def merge_lists(my_list, alices_list):
    res = list()
    n1 = len(my_list)
    n2 = len(alices_list)
    ctr1 = 0
    ctr2 = 0
    while True:
        if len(res) == (n1 + n2):
            break
        if ctr1 < n1 and ctr2 < n2:
            if my_list[ctr1] < alices_list[ctr2]:
                res.append(my_list[ctr1])
                ctr1 += 1
            elif my_list[ctr1] > alices_list[ctr2]:
                res.append(alices_list[ctr2])
                ctr2 += 1
            else:
                res.append(my_list[ctr1])
                ctr1 += 1
                res.append(alices_list[ctr2])
                ctr2 += 1
        if ctr1 == len(my_list) and ctr2 < n2:
            res.append(alices_list[ctr2])
            ctr2+=1
        elif ctr2 == len(alices_list) and ctr1 < n1:
            res.append(my_list[ctr1])
            ctr1 += 1

    return res


print(merge_lists([2, 4, 6, 8], [1, 7]))



# solution

# def merge_lists(my_list, alices_list):
#     # Set up our merged_list
#     merged_list_size = len(my_list) + len(alices_list)
#     merged_list = [None] * merged_list_size
#
#     current_index_alices = 0
#     current_index_mine = 0
#     current_index_merged = 0
#     while current_index_merged < merged_list_size:
#         is_my_list_exhausted = current_index_mine >= len(my_list)
#         is_alices_list_exhausted = current_index_alices >= len(alices_list)
#         if (not is_my_list_exhausted and
#                 (is_alices_list_exhausted or
#                  my_list[current_index_mine] < alices_list[current_index_alices])):
#             # Case: next comes from my list
#             # My list must not be exhausted, and EITHER:
#             # 1) Alice's list IS exhausted, or
#             # 2) the current element in my list is less
#             #    than the current element in Alice's list
#             merged_list[current_index_merged] = my_list[current_index_mine]
#             current_index_mine += 1
#         else:
#             # Case: next comes from Alice's list
#             merged_list[current_index_merged] = alices_list[current_index_alices]
#             current_index_alices += 1
#
#         current_index_merged += 1
#
#     return merged_list