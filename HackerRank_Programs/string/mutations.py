# We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).
#
# Let's try to understand this with an example.
#
# You are given an immutable string, and you want to make changes to it.
# Sample Input:
# STDIN           Function
# -----           --------
# abracadabra     s = 'abracadabra'
# 5 k             position = 5, character = 'k'
# Sample Output: abrackdabra

def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:]
    return string


s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)