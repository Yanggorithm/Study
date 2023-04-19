# import sys
# input = sys.stdin.readline
from pprint import pprint
from collections import deque

dx = [-1, 1, 0, 0, 0]
dy = [0, 0, -1, 1, 0]

# 금으로 막혀있으면 '#', 비어있는칸 '.'
# 시작지점 'S', 탈출지점 'E'

# L은 층수, R은 세로, C는 가로
def is_valid(rx, ry):
    return 0 <= rx < R and 0 <= ry < C

def dfs(x, y, flr_cnt, result):
    global min_v
    if floor[flr_cnt][x][y] == 'E':
        min_v = min(min_v, visited[flr_cnt][x][y])
        return

    if min_v < visited[flr_cnt][x][y]:
        return

    for d in range(5):
        nx = x + dx[d]
        ny = y + dy[d]
        if is_valid(nx, ny) and not floor[flr_cnt][nx][ny] != '#' and not visited[flr_cnt][nx][ny]:
            visited[flr_cnt][nx][ny] = visited[flr_cnt][x][y] + 1
            dfs(nx, ny, flr_cnt, result + 1)
            visited[flr_cnt][nx][ny] -= 1

            if d == 4 and L > 1:
                if floor[flr_cnt + 1][nx][ny] != '#':
                    visited[flr_cnt + 1][nx][ny] = visited[flr_cnt][x][y] + 1
                    dfs(nx, ny, flr_cnt + 1, result + 1)
                    visited[flr_cnt][nx][ny] -= 1

while True:
    L, R, C = map(int, input().split())
    if L == 0:
        break

    floor = []
    cnt = 0
    temp = []
    sx, sy, ex, ey = 0, 0, 0, 0
    for i in range(L * R + L):
        if cnt == R:
            print(temp)
            for i in range(R):
                for j in range(C):
                    if temp[i][j] == 'S':
                        sx, sy = i, cnt
                    elif temp[i][j] == 'E':
                        ex, ey = i, cnt
            blank = input()
            floor.append(temp)
            temp = []
            cnt = 0
        else:
            temp.append(list(input()))
            cnt += 1

    min_v = 9999999
    visited = [[[0] * C for _ in range(R)] for _ in range(L)]
    dfs(sx, sy, 0, 0)
    if min_v == 999999:
        print('Trapped!')
    else:
        print(f'Escaped in {min_v} minute(s).')
