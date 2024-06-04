# Input Format:
# The first line contains integer n, the number of elements in the set s.
# The second line contains n space separated elements of set s. All of the elements are non-negative integers, less than or equal to 9.
# The third line contains integer n, the number of commands.
# The next n lines contains either pop, remove and/or discard commands followed by their associated value.
#
# Output Format:
# Print the sum of the elements of set s on a single line.

n = int(input())
s = set(map(int, input().split()))
m = int(input())
for i in range(m):
    commands = input().split()
    method = str(commands[0].lower())
    # print(method)
    if method == "remove":
        s.remove(int(commands[1]))
    elif method == "pop":
        s.pop()
    elif method == "discard":
        s.discard(int(commands[1]))
print(sum(s))
