# Input Format:
# The first line contains integers n and m separated by a space.
# The second line contains n integers, the elements of the array.
# The third and fourth lines contain m integers, a and b, respectively.
#
# Output Format:
# Output a single integer, your total happiness.

n, m = map(int, input().split())
c = list(map(int, input().split()))
happiness = 0
a = set(map(int, input().split()))
b = set(map(int, input().split()))
for i in c:
    if int(i) in a:
        happiness += 1
    elif int(i) in b:
        happiness -= 1
print(happiness)
