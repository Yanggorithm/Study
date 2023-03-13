import sys
from collections import deque
input = sys.stdin.readline
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def is_valid(nr, nc):
    return 0 <= nr < N and 0 <= nc < M

def no_crossroads(r, c):
    cnt = 0
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if is_valid(nr, nc) and t_map[nr][nc] == "L":
            cnt += 1
    return cnt == 1

N, M = map(int, input().split())
t_map = []
Land = deque()
for r in range(N):
    t_map.append(list(input().strip()))
    for c in range(M):
        if t_map[r][c] == "L":
            Land.append((r, c))
max_distance = 0
for sr, sc in Land:
    q = deque()
    q.append((sr, sc))
    visited = [[-1] * M for _ in range(N)]
    visited[sr][sc] = 0
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if is_valid(nr, nc) and visited[nr][nc] == -1 and t_map[nr][nc] == "L":
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr, nc))
                max_distance = max(max_distance, visited[nr][nc])
print(max_distance)