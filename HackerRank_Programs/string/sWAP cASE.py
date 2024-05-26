# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
# input: HackerRank.com presents "Pythonist 2".
# output: hACKERrANK.COM PRESENTS "pYTHONIST 2".

def swap_case(word):
    swaped = ""
    for i in word:
        if i == i.lower():
            swaped += i.upper()
        elif i == i.upper():
            swaped += i.lower()
    return swaped


s = input()
result = swap_case(s)
print(result)
