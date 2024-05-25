# Given an integer, n, and n space-separated integers as input, create a tuple, t, of those n integers. Then compute and print the result of hash(t).
# input:
# 2
# 1 2
# Output: 3713081631934410656

n = int(input("n"))
integer_list = map(int, input("l").split())
t = tuple(integer_list)
print(hash(t))
