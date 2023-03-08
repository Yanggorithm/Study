# 테스트 케이스 6번부터 오답
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]

    visited = [[-1] * n for _ in range(n)]

    q = deque([(0, 0)])
    visited[0][0] = 0
    while q:
        ci, cj = q.popleft()
        if ci == n-1 and cj == n-1:
            break

        for d in range(4):
            ni, nj = ci+dx[d], cj+dy[d]
            if 0 <= ni < n and 0 <= nj < n:
                if visited[ni][nj] == -1:
                    visited[ni][nj] = arr[ni][nj] + visited[ci][cj]
                    q.append((ni, nj))
                elif visited[ni][nj] > arr[ni][nj] + visited[ci][cj]:
                    visited[ni][nj] = arr[ni][nj] + visited[ci][cj]
                    q.append((ni, nj))

    print(f"#{tc} {visited[n-1][n-1]}")

"""
1
5
01111
03000
02010
00010
11110
"""