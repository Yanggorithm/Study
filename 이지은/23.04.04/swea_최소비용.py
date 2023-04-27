from collections import deque
t = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solve(q):
    while q:
        ci, cj = q.popleft()

        for d in range(4):
            ni, nj = ci+dx[d], cj+dy[d]
            if 0 <= ni < n and 0 <= nj < n:
                t = 1
                if arr[ci][cj] < arr[ni][nj]:
                    t += arr[ni][nj] - arr[ci][cj]
                if visited[ni][nj] > visited[ci][cj] + t:
                    visited[ni][nj] = visited[ci][cj] + t
                    q.append((ni, nj))

for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[10000]*n for _ in range(n)]
    visited[0][0] = 0
    q = deque([(0,0)])
    solve(q)
    print(f"#{tc} {visited[n-1][n-1]}")