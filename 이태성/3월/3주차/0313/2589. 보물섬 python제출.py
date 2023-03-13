# 2589 보물섬
import sys
from collections import deque
input = sys.stdin.readline

Deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]

N, M = map(int, input().split())
world = list(input().rstrip() for _ in range(N))


def bfs(row, column):
    queue = deque()
    queue.append((row, column))
    visited = [[0] * M for _ in range(N)]
    visited[row][column] = 1
    depth = -1
    while queue:
        depth += 1
        for _ in range(len(queue)):
            y, x = queue.popleft()
            for dy, dx in Deltas:
                ny = y + dy
                nx = x + dx
                if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                    if world[ny][nx] == 'L':
                        visited[ny][nx] = 1
                        queue.append((ny, nx))
    return depth


res = 0
for i in range(N):
    for j in range(M):
        if world[i][j] == 'L':
            res = max(bfs(i, j), res)
print(res)