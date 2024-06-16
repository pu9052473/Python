# Input Format:
# The first line contains the first integer,a, and the second line contains the second integer,b.
#
# Output Format:
# Print the result as described above.

a = int(input())
b = int(input())
result = divmod(a, b)
print(result[0])
print(result[1])
print(result)
