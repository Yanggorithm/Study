import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def is_valid(sx, sy):
    return 0 <= sx < N and 0 <= sy < N

def bfs1(x, y, cnt, value):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if is_valid(nx, ny) and map_v[nx][ny] == value and not visited_1[nx][ny]:
                visited_1[nx][ny] = cnt
                q.append((nx, ny))


def bfs2(x, y, cnt, value):
    t = deque()
    t.append((x, y))

    while t:
        x, y = t.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if is_valid(nx, ny) and not visited_2[nx][ny]:
                if value in GR and map_v[nx][ny] in GR:
                    visited_2[nx][ny] = cnt
                    t.append((nx, ny))
                elif value in B and map_v[nx][ny] in B:
                    visited_2[nx][ny] = cnt
                    t.append((nx, ny))


N = int(input())

map_v = [list(input().strip()) for _ in range(N)]

visited_1 = [[0] * N for _ in range(N)]
visited_2 = [[0] * N for _ in range(N)]

GR = ['G', 'R']
B = ['B']

result1, result2 = 1, 1

for i in range(N):
    for j in range(N):
        if not visited_1[i][j]:
            visited_1[i][j] = result1
            bfs1(i, j, result1, map_v[i][j])
            result1 += 1
        if not visited_2[i][j]:
            visited_2[i][j] = result2
            bfs2(i, j, result2, map_v[i][j])
            result2 += 1

print(result1 - 1, result2 - 1)