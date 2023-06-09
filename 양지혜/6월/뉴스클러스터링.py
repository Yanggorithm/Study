def solution(str1, str2):
    answer = 0

    str11 = []
    for i in range(0, len(str1)+1):
        # 영어문자와 공백, 특수문자 처리
        # 영어 대문자 소문자 같게 어떻게 하지?
        # 다 대문자로 변환하자
        word1 = str1[i:i+2].upper()
        if word1.isalpha() and len(word1) == 2:
            str11.append(word1)

    str22 = []
    for i in range(0, len(str2)+1):
        word2 = str2[i:i+2].upper()
        if word2.isalpha() and len(word2) == 2:
            str22.append(word2)
    print("str11:", str11)
    print("str22:", str22)

    # 교집합
    # A = []
    # for i in str11:
    #     if i in str22:
    #         A.append(i)
    # print("교집합 A:",A)

    # 합집합
    # temp = []

    # for j in str22:
    #     if j not in str11:
    #         temp.append(j)
    # B = str11 + temp
    # print("합집합 B:", B)

    # 공집합인 경우
    # if len(A) == 0 and len(B) == 0:
    #     answer = 1 * 65536
    # else:

    #     answer = int((len(A)/len(B)) * 65536)
    # return answer

    # 다른 풀이방법
    # 교집합
    A = 0
    # 합집합
    B = 0
    if str11 == str22:
        return 65536
    for i in str11:
        if i in str22:
            str22.remove(i)
            A += 1
    B = len(str11 + str22)
    answer = int((A/B)*65536)

    return answer


str111 = "aa1+aa2"
str222 = "AAAA12"
solution(str111, str222)