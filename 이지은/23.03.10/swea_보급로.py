# 테스트 케이스 6번부터 오답
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

t = int(input())
q = deque([])
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]

    visited = [[0] * n for _ in range(n)]
    time = [[0]*n for _ in range(n)]

    q.append((0,0))
    visited[0][0] = 1

    while q:
        ci, cj = q.popleft()

        for d in range(4):
            ni, nj = ci+dx[d], cj+dy[d]
            if 0 <= ni < n and 0 <= nj < n:
                if visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    time[ni][nj] = time[ci][cj] + arr[ni][nj]
                    q.append((ni, nj))
                else:
                    if time[ni][nj] > time[ci][cj] + arr[ni][nj]:
                        time[ni][nj] = time[ci][cj] + arr[ni][nj]
                        q.append((ni, nj))

    print(f"#{tc} {time[n-1][n-1]}")