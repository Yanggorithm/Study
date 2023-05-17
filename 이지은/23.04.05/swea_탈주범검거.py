from collections import deque

t = int(input())

"""
1: 상하좌우
2: 상하
3: 좌우
4: 상우
5: 하우
6: 하좌
7: 상좌

상행 : 1,2,5,6
하행 : 1,2,4,7
좌행 : 1,3,4,5
우행 : 1,3,6,7

bfs
"""
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

next_d = [[1, 2, 5, 6], [1, 2, 4, 7], [1, 3, 4, 5], [1, 3, 6, 7]]
direction = [
    [],
    [0,1,2,3],
    [0,1],
    [2,3],
    [0,3],
    [1,3],
    [1,2],
    [0,2]
]
for tc in range(1, t+1):
    n, m, r, c, l = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    visited = [[0] * m for _ in range(n)]
    time = 0
    q = deque([])
    q.append((r, c))
    visited[r][c] = 1

    while q:
        ci, cj = q.popleft()
        for d in direction[arr[ci][cj]]:
            ni, nj = ci+dx[d], cj+dy[d]
            if 0 <= ni < n  and 0 <= nj < m and visited[ni][nj] == 0 and (arr[ni][nj] in next_d[d]):
                q.append((ni, nj))
                visited[ni][nj] = visited[ci][cj] + 1
    
    ans = 0
    for i in range(n):
        for j in range(m):
            if 0 < visited[i][j] <= l:
                ans += 1
    
    print(f"#{tc} {ans}")