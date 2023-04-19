from collections import deque

def bfs(si, sj, ei, ej):
    q = deque()
    q.append((si, sj))
    visit = [[0] * m for _ in range(n)]
    visit[si][sj] = 1

    while q:

        ci, cj = q.popleft()
        if (ci, cj) == (ei, ej):
            return visit[ei][ej]

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < m and visit[ni][nj] == 0 and maze[ni][nj] == 1:
                q.append((ni, nj))
                visit[ni][nj] = visit[ci][cj] + 1

n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]
si, sj = 0, 0
ei, ej = n-1, m-1
print(bfs(si, sj, ei, ej))
