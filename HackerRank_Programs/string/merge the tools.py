def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        # print(string[i: i+k])
        my_str = ""
        for s in string[i: i+k]:
            if s not in my_str:
                my_str += s
        print(my_str)


string, k = input("s"), int(input("k"))
merge_the_tools(string, k)
