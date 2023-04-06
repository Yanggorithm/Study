import sys
sys.stdin = open('보호필름.txt', 'r')
from pprint import pprint


import copy

def check(n_list):
    # 조건에 맞게 연속적인 값이 존재하는지 판단하는 함수
    for i in range(W):
        cnt = 1
        for j in range(1, D):
            if n_list[j][i] == n_list[j - 1][i]:
                cnt += 1
            else:
                cnt = 1

            if cnt >= K:
                break

        if cnt < K:
            return 0
    return 1


def backtracking(depth, k, select):
    # 줄을 0, 1로 만들어 백트래킹 진행
    global min_v
    if depth >= min_v:
        return

    if depth == select:
        if check(film):
            min_v = min(min_v, depth)
        return

    for i in range(k, D):
        for d in range(2):
            film[i] = z_o_list[d]
            backtracking(depth + 1, i + 1, select)
            film[i] = temp_list[i]

T = int(input())

for test_case in range(1, T + 1):
    D, W, K = map(int, input().split())
    # D : 세로, W : 가로, K : 합격기준

    film = [list(map(int, input().split())) for _ in range(D)]
    # film의 1값은 B 0값은 A
    temp_list = copy.deepcopy(film)

    z_o_list = [[0] * W, [1] * W]
    if check(film):
        # 원본 필름이 통과 되면 min_v = 0 설정후 출력
        min_v = 0
    else:
        min_v = 999999
        for i in range(1, D + 1):
            # 조합을 할 때 몇개 뽑을 지 정하는 for문
            backtracking(0, 0, i)
            if min_v < 999999:
                break

    print(f'#{test_case} {min_v}')
