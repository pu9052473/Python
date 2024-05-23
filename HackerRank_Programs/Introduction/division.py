# The provided code stub reads two integers, a and b, from STDIN.
#
# Add logic to print two lines. The first line should contain the result of integer division, a // b. The second line should contain the result of float division, a / b.
#
# No rounding or formatting is necessary.

a = int(input())
b = int(input())

int_div = a // b
print(int_div)

float_div = a / b
print(float_div)
