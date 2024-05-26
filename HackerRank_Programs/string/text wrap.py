# You are given a string s and width w.
# Your task is to wrap the string into a paragraph of width w.
# input:
# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4
# output:
# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ
def wrap(string, max_width):
    result = ""
    for i in range(0, len(string), max_width): # we take here step size "max_width" because like we have their value 4 so loop start from 0 and print the string[0:4] for first iteration, now the loop value start from 4 so now this print string[4:8] so doing this becase we have to take string in the peice of max_width size
        result += string[i:i+max_width] + "\n"
    return result


string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)