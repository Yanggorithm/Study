import sys
from collections import deque
input = sys.stdin.readline
dr = [-1, 1, 0, 0, -1, 1, -1, 1]
dc = [0, 0, -1, 1, -1, 1, 1, -1]

def is_valid(nr, nc):
    return 0 <= nr < h and 0 <= nc < w

def bfs(sr, sc):
    q = deque()
    q.append((sr, sc))
    visited[sr][sc] = 1
    while q:
        r, c = q.popleft()
        for d in range(8):
            nr = r + dr[d]
            nc = c + dc[d]
            if is_valid(nr, nc) and visited[nr][nc] == 0 and earth[nr][nc] == 1:
                visited[nr][nc] = 1
                q.append((nr, nc))

while True:
    w, h = map(int, input().split())
    if (w, h) == (0, 0):
        break
    earth = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    island = 0
    for r in range(h):
        for c in range(w):
            if earth[r][c] == 1 and visited[r][c] == 0:
                bfs(r, c)
                island += 1
    print(island)