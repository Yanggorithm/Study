# 프로그래머스 가장 가까운 같은 글자
# 주석 처리 코드는 실패. 왜?

# def solution(s):
#     check = {}
#     answer = [0] * len(s)
#     for i, l in enumerate(s):
#         if not check.get(l):
#             check[l] = i
#             answer[i] = -1
#         else:
#             answer[i] = i - check[l]
#             check[l] = i
#     return answer

def solution(s):
    check = {}
    answer = [0] * len(s)
    for i, l in enumerate(s):
        if l not in check:
            check[l] = i
            answer[i] = -1
        else:
            answer[i] = i - check[l]
            check[l] = i
    return answer