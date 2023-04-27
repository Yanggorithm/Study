# pypy 통과, python 시간초과
import sys
input = sys.stdin.readline

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 한 육지에서 다른 육지로 거리를 구한다 dfs
# 가장 긴 시간이 걸리는 육지 두곳을 구한다

r, c = map(int, input().strip().split())
arr = []
land = []
for i in range(r):
    t = list(input().strip())
    arr.append(t)
    for j in range(c):
        if t[j] == "L":
            land.append((i, j))
q = deque([])
time = 0
longest = []
for li, lj in land:
    visited = [[0]*c for _ in range(r)]
    visited[li][lj] = 1
    q.append((li, lj))
    while q:
        ci, cj = q.popleft()
        for d in range(4):
            ni, nj = ci+dx[d], cj+dy[d]
            if 0 <= ni < r and 0 <= nj < c and arr[ni][nj] == "L" and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[ci][cj] + 1
                if visited[ni][nj] > time:
                    time = visited[ni][nj]

print(time-1)