def minion_game(string):
    # your code goes here
    stuart_score = 0
    kevin_score = 0

    # first simple function
    # for i in range(len(string)):
    #     for j in range(i+1, len(string)+1):
    #         substrings.append((string[i:j]))
    # print(substrings)

    # for s in range(len(substrings)):
    #     if substrings[s][0] in vowels:
    #         kevin_score += 1
    #     else:
    #         stuart_score += 1

    # second merge of the first function
    # for i in range(len(string)):
    #     for j in range(i + 1, len(string) + 1):
    #         # print(string[i]) this is the first element of substring
    #         if string[i] in vowels:
    #             kevin_score += 1
    #         else:
    #             stuart_score += 1

    # for exp:input = banana, first char is b then the chance of the first character is "b" is the length - index[b],
    for index, char in enumerate(string):
        if char in "AEIOU":
            kevin_score += len(string) - index
        else:
            stuart_score += len(string) - index

    # print(stuart_score)
    # print(kevin_score)

    if stuart_score > kevin_score:
        print("Stuart", stuart_score)
    elif kevin_score > stuart_score:
        print("Kevin", kevin_score)
    else:
        print("Draw")


input_string = input().upper()
minion_game(input_string)
