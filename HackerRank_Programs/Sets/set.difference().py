# Input Format:
# The first line contains an integer,n, the number of students who have subscribed to the English newspaper.
# The second line contains n space separated roll numbers of those students.
# The third line contains b, the number of students who have subscribed to the French newspaper.
# The fourth line contains b space separated roll numbers of those students.
#
# Output Format:
# Output the total number of students who are subscribed to the English newspaper only.
n = int(input())
rollNo_E = set(map(int, input().split()))
b = int(input())
rollNo_F = set(map(int, input().split()))
print(len(rollNo_E.difference(rollNo_F)))
