# Input Format:
# The first line contains an integer n, the total number of country stamps.
# The next n lines contains the name of the country where the stamp is from.
#
# Output Format:
# Output the total number of distinct country stamps on a single line.

n = int(input())
countrys = set()
for i in range(n):
    countrys.add(input())
print(len(countrys))
