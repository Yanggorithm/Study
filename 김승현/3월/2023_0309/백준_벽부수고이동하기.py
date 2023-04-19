from collections import deque

N, M = map(int, input().split())

block = [list(map(int, input())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(sx, sy):
    visited = [[0] * M for _ in range(N)]
    q = deque()
    q.append((sx, sy))
    visited[sx][sy] = 0
    flag = 0

    while q:
        x, y = q.popleft()
        if x == 0 and y == 0:
            flag = 0

        if x == N - 1 and y == M - 1:
            return visited[N - 1][M - 1]

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if flag == 0:
                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                    if block[nx][ny] == 1:
                        block[nx][ny] = 0
                        flag = 1
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
            else:
                if 0 <= nx < N and 0 <= ny < M and block[nx][ny] != 1 and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

    return -1

print(bfs(0,0))