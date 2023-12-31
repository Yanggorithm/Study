def solution(str1, str2):
    jacard1 = dict()
    jacard2 = dict()

    word = ""
    for i in range(1, len(str1)):
        word = (str1[i - 1] + str1[i]).lower()
        if word.isalpha():
            if jacard1.get(word) and jacard1.get(word) >= 1:
                jacard1[word] += 1
            else:
                jacard1[word] = 1

    for j in range(1, len(str2)):
        word = (str2[j - 1] + str2[j]).lower()
        if word.isalpha():
            print(word)
            if jacard2.get(word) and jacard2.get(word) >= 1:
                jacard2[word] += 1
            else:
                jacard2[word] = 1

    print(jacard1)
    print(jacard2)
    intersection_jacard = 0
    for k in jacard2.keys():
        if jacard1.get(k):
            intersection_jacard += (min(jacard1[k], jacard2[k]))
    union_jacard = sum(jacard1.values()) + sum(jacard2.values()) - intersection_jacard

    answer = 0
    if union_jacard:
        answer = int(intersection_jacard / union_jacard * 65536)
    else:
        answer = 65536
    return answer