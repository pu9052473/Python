# Input Format:
# The first line contains the number of elements in set a.
# The second line contains the space separated list of elements in set a.
# The third line contains integer n, the number of other sets.
# The next 2*n lines are divided into n parts containing two lines each.
# The first line of each part contains the space separated entries of the operation name and the length of the other set.
# The second line of each part contains space separated list of elements in the other set.
#
# Output Format:
# Output the sum of elements in set a.

num_a = int(input())
a = set(map(int, input().split()))
n = int(input())
for i in range(n):
    commands = input().split()
    methods = str(commands[0].lower())
    elements = set(map(int, input().split()))
    if methods == "intersection_update":
        a.intersection_update(elements)
    if methods == "update":
        a.update(elements)
    if methods == "symmetric_difference_update":
        a.symmetric_difference_update(elements)
    if methods == "difference_update":
        a.difference_update(elements)
print(sum(a))
