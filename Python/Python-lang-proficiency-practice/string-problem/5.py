"""
Copyrights Reserved 
Developed By- Anukkrit Shanker
"""


def solve(s):

    string_arr = list(s)
    if string_arr[0] != ' ':
        string_arr[0] = string_arr[0].capitalize()
    for i in range(len(string_arr)):
        if string_arr[i] == ' ':
            string_arr[i+1]=string_arr[i+1].capitalize()
    res = ''
    return res.join(string_arr)

print(solve("hello   world  lol"))