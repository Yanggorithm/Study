import sys
sys.stdin = open('3월\\양고리즘3_4주차_백트래킹\\20230322\\숫자만들기.txt', 'r')
from time import time
T = int(input())


# def calcul(a, b, cal_char):
#     if cal_char == cal[0]:
#         return a + b
#     elif cal_char == cal[1]:
#         return a - b
#     elif cal_char == cal[2]:
#         return a * b
#     else:
#         return int(a / b)
#
#
# def dfs(result, idx):
#     if idx >= N - 1:
#         global min_v, max_v
#         if result < min_v:
#             min_v = result
#
#         if result > max_v:
#             max_v = result
#         return
#
#     for i in range(N - 1):
#         if not visited[i]:
#             visited[i] = 1
#             dfs(calcul(result, num_list[idx+1], cal_res[i]), idx+1)
#             visited[i] = 0
#
#
# for test_case in range(1, T + 1):
#     N = int(input())
#
#     cal = ['+', '-', '*', '/']
#     cal_list = list(map(int, input().split()))
#
#     num_list = list(map(int, input().split()))
#
#     cal_res = []
#     for i in range(4):
#         cal_res.extend(cal_list[i] * cal[i])
#
#     min_v = 99999999
#     max_v = -999999999
#     visited = [0] * (N - 1)
#     dfs(num_list[0], 0)
#
#     print(f'#{test_case} {max_v - min_v}')





# T = int(input())

cal = ['+', '-', '*', '/']

def cal_cul(a, b, cal_char):
    if cal_char == 0:
        return a + b
    elif cal_char == 1:
        return a - b
    elif cal_char == 2:
        return a * b
    else:
        return int(a/b)


def dfs(result, idx):
    if idx >= N - 1:

        global min_v, max_v
        if result < min_v:
            min_v = result

        if result > max_v:
            max_v = result

        return

    for i in range(4):
        if cal_list[i]:
            cal_list[i] -= 1
            dfs(cal_cul(result, num_list[idx + 1], i), idx + 1)
            cal_list[i] += 1

start = time()
for test_case in range(1, T + 1):
    N = int(input())
    # 연산자의 개수 + - * /
    cal_list = list(map(int, input().split()))

    cal_res = []
    for i in range(4):
        cal_res.extend(cal[i] * cal_list[i])
    # 수식에 사용되는 숫자
    num_list = list(map(int, input().split()))

    min_v = 99999999
    max_v = -999999999

    dfs(num_list[0], 0)

    print(f'#{test_case} {max_v - min_v}')
end = time()
print(f'걸리는시간 : {end - start}')