import sys
from collections import deque
input = sys.stdin.readline

def is_valid(nr, nc):
    return 0 <= nr < N and 0 <= nc < M

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(sr, sc):
    q = deque()
    q.append((sr, sc))
    visited[sr][sc] = 1
    area = 1
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if is_valid(nr, nc) and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                q.append((nr, nc))
                area += 1
    return area

M, N, K = map(int, input().split())
visited = [[0] * M for _ in range(N)]
for _ in range(K):
    r, c, p, q = map(int, input().split())
    for i in range(r, p):
        for j in range(c, q):
            visited[i][j] = 1
total = []
cnt = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            cnt += 1
            total.append(bfs(i, j))
total.sort()
print(cnt)
print(*total)