# The first line contains the integer, n, the size of arr.
# The second line contains the n space-separated integers,arr[i].

def average(array):
    # your code goes here
    s = 0
    array = set(array)
    for i in array:
        s += i
    ave = s / len(array)
    return ave


n = int(input())
arr = list(map(int, input().split()))
result = average(arr)
print(result)
