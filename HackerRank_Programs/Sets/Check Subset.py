# Input Format:
# The first line will contain the number of test cases,t.
# The first line of each test case contains the number of elements in set a.
# The second line of each test case contains the space separated elements of set a.
# The third line of each test case contains the number of elements in set b.
# The fourth line of each test case contains the space separated elements of set b.
#
# Output Format:
# Output True or False for each test case on separate lines.

n = int(input())
for i in range(n):
    # is_sub = "True"
    num_a = int(input())
    a = set(map(int, input().split()))
    num_b = int(input())
    b = set(map(int, input().split()))
    print(a.issubset(b))
    # for j in a:
    #     if j not in b:
    #         is_sub = "False"
    # print(is_sub)
