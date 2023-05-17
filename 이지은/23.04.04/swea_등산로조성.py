from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solve(ci, cj, chance):
    global ans
    ans = max(visited[ci][cj], ans)

    for d in range(4):
        ni, nj = ci + dx[d], cj + dy[d]
        if not (0 <= ni < n and 0 <= nj < n) or visited[ni][nj]:
            continue
        if arr[ci][cj] > arr[ni][nj]:
            visited[ni][nj] = visited[ci][cj] + 1
            solve(ni, nj, chance)
            visited[ni][nj] = 0
        elif chance and arr[ni][nj] - k < arr[ci][cj]:
            visited[ni][nj] = visited[ci][cj] + 1
            tmp = arr[ni][nj]
            arr[ni][nj] = arr[ci][cj] - 1
            solve(ni, nj, chance -1)
            visited[ni][nj] = 0
            arr[ni][nj] = tmp


t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())
    arr = []
    h = 0 
    for _ in range(n):
        t = list(map(int, input().split()))
        h = max(h, max(t))
        arr.append(t)
        
    visited = [[0]*n for _ in range(n)]    
    ans = 0
    for si in range(n):
        for sj in range(n):
            if arr[si][sj] == h:
                visited[si][sj] = 1
                solve(si, sj, 1)
                visited[si][sj] = 0
    
    print(f"#{tc} {ans}")
