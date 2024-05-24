# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.
# example:
# 5
# 2 2 5 5 6 6
# output:
# 5

n = int(input("n"))
# my_list = [int(input()) for i in range(n)]
my_list = map(int, input("a").split())
largest = -99999999999999999999999999999999
runnerUpScore = -99999999999999999999999999999999
new_set = set(my_list)

print(new_set)
for i in new_set:
    if i > largest:
        largest = i
print(largest)

new_set.remove(largest)
print(new_set)

for i in new_set:
    if i > runnerUpScore:
        runnerUpScore = i

print(runnerUpScore)

# # another for this
# n = int(input("n"))
# my_list = map(int, input("a").split())
# sortedList = sorted(set(my_list))
# print(sortedList[-2])




