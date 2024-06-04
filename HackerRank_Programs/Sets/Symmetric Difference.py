# Input Format :
# The first line of input contains an integer,m.
# The second line contains m space-separated integers.
# The third line contains an integer,n.
# The fourth line contains n space-separated integers.
#
# Output Format:
# Output the symmetric difference integers in ascending order, one per line.

m = int(input())
listInputA = input().split()
a = set(map(int, listInputA))

n = int(input())
listInputB = input().split()
b = set(map(int, listInputB))

difference = sorted(a.difference(b).union(b.difference(a)))
for i in difference:
    print(i)
