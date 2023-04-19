import sys
from collections import deque
# import copy
input = sys.stdin.readline


T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def fire_bfs(q, h):
    global cnt

    while q:
        fire_size = len(q)
        for _ in range(fire_size):
            x, y = q.popleft()

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if is_valid(nx, ny) and town[nx][ny] != '#' and not fire_v[nx][ny]:
                    q.append((nx, ny))
                    fire_v[nx][ny] = 1

        human_size = len(h)
        for _ in range(human_size):
            hx, hy = h.popleft()
            for d in range(4):
                hnx = hx + dx[d]
                hny = hy + dy[d]
                if is_valid(hnx, hny) == 0:
                    return
                else:
                    if town[hnx][hny] == '.' and not fire_v[hnx][hny]:
                        h.append((hnx, hny))
                        fire_v[hnx][hnx] = 2

        cnt += 1

        if len(h) == 0:
            cnt = "IMPOSSIBLE"
            return



def is_valid(sx, sy):
    return 0 <= sx < c and 0 <= sy < r


for test_case in range(T):
    r, c = map(int, input().split())

    town = [list(input()) for _ in range(c)]
    fire_v = [[0] * r for _ in range(c)]
    fire = deque()
    human = deque()

    # 상근이의 초기 위치
    for i in range(c):
        for j in range(r):
            if town[i][j] == '*':
                fire.append((i, j))
                fire_v[i][j] = 1
            elif town[i][j] == '@':
                human.append((i, j))
                fire_v[i][j] = 2

    cnt = 1

    fire_bfs(fire, human)

    if cnt == 1:
        print('IMPOSSIBLE')
    else:
        print(cnt)