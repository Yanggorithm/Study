import sys
from collections import deque

input = sys.stdin.readline

def bfs(q):
    global max_v
    while q:
        z, x, y = q.popleft()

        for d in range(6):
            nx = x + dx[d]
            ny = y + dy[d]
            nz = z + dz[d]
            if is_valid(nx, ny, nz) and tomato[nz][nx][ny] == '0' and not visited[nz][nx][ny]:
                visited[nz][nx][ny] = visited[z][x][y] + 1
                q.append((nz, nx, ny))
                max_v = max(max_v, visited[nz][nx][ny])

    for i in range(H):
        for j in range(N):
            if visited[i][j].count(0):
                return -1

    else:
        return max_v - 1

def is_valid(sx, sy, sz):
    return 0 <= sx < N and 0 <= sy < M and 0 <= sz < H


dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

M, N, H = map(int, input().split())

tomato = []

real_to = deque()

visited = [[[0] * M for _ in range(N)] for _ in range(H)]
for i in range(H):
    temp = []
    for j in range(N):
        temp.append(list(input().split()))

        for t in range(M):
            if temp[j][t] == '1':
                real_to.append((i, j, t))
                visited[i][j][t] = 1
                max_v = 1
            elif temp[j][t] == '-1':
                visited[i][j][t] = -1


    tomato.append(temp)

print(bfs(real_to))