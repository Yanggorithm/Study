# N = int(input())
#
# n_list = [list(map(int, input().split())) for _ in range(N)]
#
# z_cnt = 0
# o_cnt = 0
#
#
# def check(x, y, n):
#     global z_cnt, o_cnt
#     color = n_list[x][y]
#     for i in range(x, x + n):
#         for j in range(y, y + n):
#             if color != n_list[i][j]:
#                 check(x, y, n // 2)
#                 check(x + n // 2, y, n // 2)
#                 check(x, y + n // 2, n // 2)
#                 check(x + n // 2, y + n // 2, n // 2)
#                 return
#
#     if color == 0:
#         z_cnt += 1
#     else:
#         o_cnt += 1
#
# check(0, 0, N)
#
# print(z_cnt)
# print(o_cnt)
#

import sys

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = []


def solution(x, y, N):
    color = paper[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if color != paper[i][j]:
                solution(x, y, N // 2)
                solution(x, y + N // 2, N // 2)
                solution(x + N // 2, y, N // 2)
                solution(x + N // 2, y + N // 2, N // 2)
                return
    # if color == 0 :
    #   result.append(0)
    # else :
    #   result.append(1)
    result.append(color)


solution(0, 0, N)
print(result.count(0))
print(result.count(1))
