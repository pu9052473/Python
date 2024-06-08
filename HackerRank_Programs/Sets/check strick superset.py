# Input Format:
# The first line contains the space separated elements of set A.
# The second line contains integer n, the number of other sets.
# The next n lines contains the space separated elements of the other sets.
#
# Output Format:
# Print True if set A is a strict superset of all other N sets. Otherwise, print False.

A = set(map(int, input().split()))
N = int(input())
isStrictSuperset = True

while N != 0:
    b = set(map(int, input().split()))
    if not A.issuperset(b) or A == b:
        isStrictSuperset = False
        break
    N -= 1

print(isStrictSuperset)
