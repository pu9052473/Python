def print_formatted(number):
    # your code goes here
    for i in range(1, number + 1):
        width = len(str(bin(number))) - 2

        print(str(i).rjust(width), str(oct(i)).split("o")[1].upper().rjust(width),
              str(hex(i)).split("x")[1].upper().rjust(width), str(bin(i).split("b")[1]).upper().rjust(width))
# here we conver the answer into string by "str(oct(i))", then we split the output by "o" and take the second element of that, then we convert it into uppercase then we set the position at right by "rjust" with the width of the last element of "binary - 2" because it have extra two text like "xo" , same for all


n = int(input())
print_formatted(n)
