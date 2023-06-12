# 성공코드
def solution(s, skip, index):
    answer = ''
    skip_set = set()
    for i in skip:
        skip_set.add(ord(i))

    for i in s:
        # 아스키코드값 (a:97 ~ z:122)
        temp = ord(i)
        cnt = index
        while cnt != 0:
            temp += 1

            if temp > ord('z'):
                temp = temp - ord('z') + ord('a') -1
            if temp in skip_set:
                continue
            cnt -= 1

        answer += chr(temp)
    return answer


# 실패코드
# def solution(s, skip, index):
#     answer = ''
#     skip_lst = []
#     for i in skip:
#         skip_lst.append(ord(i))
#     skip_lst = sorted(skip_lst)
#     print(skip_lst)
#     word_lst = []
#     temp = ''
#     for i in s:
#         # 아스키코드값 (a:97 ~ z:122)
#         # print(ord(i))
#         temp = ord(i) + index
#         cnt = 0
#         for j in skip_lst:
#             if ord(i) < j < temp:
#                 cnt += 1
#         temp += cnt
#         if temp > 122:
#             temp = temp - 122 +96
#         word_lst.append(chr(temp))
#
#     answer = ''.join(word_lst)
#     return answer

# 테케 (결과 : happy )
s = "aukks"
skip = "wbqd"
index = 5


# 반례 ( 결과 : zzzzzz )
# s = "zzzzzz"
# skip = "abcdefghijklmnopqrstuvwxy"
# index = 6
print(solution(s, skip, index))