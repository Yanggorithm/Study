import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def is_valid(sx, sy):
    return 0 <= sx < C and 0 <= sy < R


R, C = map(int, input().split())


tomato = [list(map(int, input().split())) for _ in range(C)]
q = deque()
visited = [[0] * R for _ in range(C)]

for i in range(C):
    for j in range(R):
        if tomato[i][j] == 1:
            visited[i][j] = 1
            q.append((i, j))
        elif tomato[i][j] == -1:
            visited[i][j] = -1

cnt = 0

while q:

    for _ in range(len(q)):
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if is_valid(nx, ny) and tomato[nx][ny] == 0 and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

max_v = 0
result = 0
for i in range(len(visited)):
    max_v = max(max_v, max(visited[i]))
    if not result:
        result = visited[i].count(0)

if result:
    print(-1)
else:
    print(max_v - 1)