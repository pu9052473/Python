# In Python, a string can be split on a delimiter.
# input: this is a string
# output: this-is-a-string

def split_and_join(line):
    # write your code here
    result = "-".join(line.split())
    return result


line = input()
result = split_and_join(line)
print(result)
