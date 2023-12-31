from pprint import pprint

from collections import deque
import copy

T = int(input())

dx = [-1, 1, 0, 0]  # 상하좌우
dy = [0, 0, -1, 1]


# 인덱스 검사 함수
def is_valid(x, y):
    return 0 <= x < H and 0 <= y < W


# 위에서 몇번째가 블록있는지 찾는 함수
def brick_check(n_list):
    brick = [0] * W

    for i in range(H):
        for j in range(W):
            if n_list[i][j] and not brick[j]:
                brick[j] = (i, j)

    return brick


# 만약 벽돌을 깨면 벽돌맵을 정리해주는 함수
def brick_sort(prev_list):
    n_list = copy.deepcopy(prev_list)
    sero_n_list = list(map(list, zip(*n_list)))

    for i in range(W):
        cnt = sero_n_list[i].count(0)

        for j in range(cnt):
            sero_n_list[i].remove(0)

        for t in range(cnt):
            sero_n_list[i].insert(0, 0)

    n_list = list(map(list, zip(*sero_n_list)))

    return n_list


# 벽돌깨는 함수
def break_brick(x, y, prev_list):
    n_list = copy.deepcopy(prev_list)
    first = n_list[x][y]

    q = deque()
    q.append((x, y, first))
    visited = [[0] * W for _ in range(H)]
    while q:
        x, y, value = q.popleft()
        n_list[x][y] = 0

        for d in range(4):
            t_x = x
            t_y = y
            for i in range(value - 1):
                nx = t_x + dx[d]
                ny = t_y + dy[d]
                if is_valid(nx, ny) and not visited[nx][ny]:
                    q.append((nx, ny, n_list[nx][ny]))
                    visited[nx][ny] = 1
                    t_x, t_y = nx, ny

    n_list = brick_sort(n_list)
    return n_list


# 재귀 진행
def check(cnt, prev_list):
    global min_v
    n_list = copy.deepcopy(prev_list)
    if cnt == N:
        count_num = 0
        for i in range(len(n_list)):
            count_num += n_list[i].count(0)
        min_v = min(min_v, (H * W) - count_num)
        if (H * W) - count_num == 0:
            return
        return

    brick = brick_check(n_list)
    for i in range(len(brick)):
        if brick[i]:
            nx, ny = brick[i][0], brick[i][1]
            next_list = break_brick(nx, ny, n_list)
            check(cnt + 1, next_list)


for test_case in range(1, T + 1):
    N, W, H = map(int, input().split())

    map_v = [list(map(int, input().split())) for _ in range(H)]
    min_v = 999999999

    check(0, map_v)
    if min_v == 999999999:
        min_v = 0
    print(f'#{test_case} {min_v}')