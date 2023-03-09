import sys
from collections import deque

m, n, k = map(int, sys.stdin.readline().strip().split())
arr = [[0] * (n) for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque([])
visited = [[0] * n for _ in range(m)]
ans = []

for i in range(m):
    for j in range(n):
        if arr[i][j] == 0 and visited[i][j] == 0:
            area = 1
            q.append((i, j))
            visited[i][j] = 1

            while q:
                ci, cj = q.popleft()
                for d in range(4):
                    ni, nj = ci + dx[d], cj + dy[d]
                    if 0 <= ni < m and 0 <= nj < n and arr[ni][nj] == 0 and visited[ni][nj] == 0:
                        visited[ni][nj] = 1
                        area += 1
                        q.append((ni, nj))
            
            ans.append(area)

print(len(ans))
print(" ".join(map(str, sorted(ans))))

