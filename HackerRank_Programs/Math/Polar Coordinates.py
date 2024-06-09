# Input Format:
# A single line containing the complex number z. Note: complex() function can be used in python to convert the input as a complex number.
#
# Output Format:
# Output two lines:
# The first line should contain the value of r.
# The second line should contain the value of a.

import cmath
z = complex(input())
r = abs(z)
a = cmath.phase(z)
print(r)
print(a)
