# The first line contains the number of students who have subscribed to the English newspaper.
# The second line contains the space separated list of student roll numbers who have subscribed to the English newspaper.
# The third line contains the number of students who have subscribed to the French newspaper.
# The fourth line contains the space separated list of student roll numbers who have subscribed to the French newspaper.
#
# Output Format:
# Output total number of students who have subscriptions to the English or the French newspaper but not both.

n = int(input())
rollNo_E = set(map(int, input().split()))
b = int(input())
rollNo_F = set(map(int, input().split()))
print(len(rollNo_E.symmetric_difference(rollNo_F)))