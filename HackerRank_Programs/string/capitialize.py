# You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.

def solve(s):
    # result = " ".join(i.capitalize() for i in s.split())
    result = ""
    i = 0
    n = len(s)

    while i < n:
        if s[i].isspace():  # this cheks that the current occurance have a space,tab,whitespace or not
            result += s[i]  # if there are space then concate in result and move to the next iteration by "+= 1"
            i += 1
        else:
            word_start = i  # if the current occurance is not space then we store its index in "word_start"
            while i < n and not s[i].isspace():  # we continue looping until the i<n or the current occurance is not any space so it will give au the full word who ends before the space
                i += 1  # we increase the index by 1 untill the condition is true
            result += s[word_start:i].capitalize()  # in this fist increase the value of i then chek the condition of while so the value of i is 1 more then the oue word so by this we get the full word by this, we take the portion which starts with the starting index of word and ends in the i

    return result


s = input()
result = solve(s)

