# Consider a list (list = []). You can perform the following commands:
#
# insert i e: Insert integer e at position i.
# print: Print the list.
# remove e: Delete the first occurrence of integer e.
# append e: Insert integer e at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.

n = int(input())
my_list = []
for i in range(n):
    commands = input().split()
    method = str(commands[0].lower())
    # print(method)
    if method == "insert":
        my_list.insert(int(commands[1]), int(commands[2]))
    elif method == "print":
        print(my_list)
    elif method == "remove":
        my_list.remove(int(commands[1]))
    elif method == "append":
        my_list.append(int(commands[1]))
    elif method == "sort":
        my_list.sort()
    elif method == "pop":
        my_list.pop()
    elif method == "reverse":
        my_list.reverse()
