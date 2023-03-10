import sys
from collections import deque
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def is_valid(nr, nc):
    return 0 <= nr < n and 0 <= nc < m

def bfs(sr, sc):
    q = deque()
    q.append((sr, sc))
    visited[sr][sc] = 1
    seaList = []

    while q:
        r, c = q.popleft()
        sw = 0
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if is_valid(nr, nc):
                if not sea[nr][nc]:
                    sw += 1
                elif sea[nr][nc] and not visited[nr][nc]:
                    q.append((nr, nc))
                    visited[nr][nc] = 1
        if sw > 0:
            seaList.append((r, c, sw))
    for y, x, zr in seaList:
        sea[y][x] = max(0, sea[y][x] - zr)

    return 1


n, m = map(int, input().split())
sea = []
ice = []
for i in range(n):
    sea.append(list(map(int, input().split())))
    for j in range(m):
        if sea[i][j]:
            ice.append((i, j))
year = 0
while ice:
    visited = [[0] * m for _ in range(n)]
    delList = []
    sector = 0
    for r, c in ice:
        if sea[r][c] and not visited[r][c]:
            sector += bfs(r, c)
        if sea[r][c] == 0:
            delList.append((r, c))
    if sector > 1:
        print(year)
        break
    ice = sorted((list(set(ice) - set(delList))))
    year += 1
if sector < 2:
    print(0)
