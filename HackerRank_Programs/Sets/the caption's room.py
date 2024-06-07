# Input Format:
# The first line consists of an integer, k, the size of each group.
# The second line contains the unordered elements of the room number list.
# Output Format
# Output the Captain's room number.(which is unique in list of c)

# my code, having little time complexity
# k = int(input())
# c = list(map(int, input().split()))
# set_c = set(c)
# my_dictionary = {}
# for i in set_c:
#     count = 0
#     for j in c:
#         if j == i:
#             count += 1
#     my_dictionary[i] = count
#
# for i, n in my_dictionary.items():
#     if n == 1:
#         print(i)

# code with less time complexity
k = int(input())
c = list(map(int, input().split()))
my_dictionary = {}
for i in c:
    if i not in my_dictionary:
        my_dictionary[i] = 1
    else:
        my_dictionary[i] += 1

for i, n in my_dictionary.items():
    if n == 1:
        print(i)
