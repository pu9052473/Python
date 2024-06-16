# Input Format:
# A single line containing integer,n.
#
# Output Format
# Print (n-1) lines as explained above.

# Let's break this down:
#
# 10 ** i // 9 creates a number with i digits, all of which are 1s. For example:
# For i = 1, 10 ** 1 // 9 results in 1.
# For i = 2, 10 ** 2 // 9 results in 11.
# For i = 3, 10 ** 3 // 9 results in 111.
#
# Multiplying this result by i gives us the repeated digit pattern we need:
# For i = 1, 1 * 1 results in 1.
# For i = 2, 11 * 2 results in 22.
# For i = 3, 111 * 3 results in 333.

for i in range(1,int(input())):
    print((10 ** i // 9) * i)
