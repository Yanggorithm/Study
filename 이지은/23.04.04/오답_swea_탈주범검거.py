from collections import deque
# 1: 상하좌우
# 2: 상하
# 3: 좌우
# 4: 상우
# 5: 하우
# 6: 하좌
# 7: 상좌
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

direction = [[],
             [0, 1, 2, 3],
             [0, 1],
             [2, 3],
             [0, 3],
             [1, 3],
             [1, 2],
             [0, 2]
             ]

# 상 : 1,2,5,6
# 하 : 1,2,4,7
# 좌 : 1,3,6,7
# 우 : 1,3,4,5
next_d = [[1,2,5,6], [1,2,4,7], [1,3,4,5], [1,3,6,7]]

def solve(q):
    cnt = 0
    while q:
        if cnt == l:
            break
        ci, cj = q.popleft()
        
        for d in direction[arr[ci][cj]]:
            ni, nj= ci+dx[d], cj+dy[d]
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and (arr[ni][nj] in next_d[d]):
                visited[ni][nj]= 1
                q.append((ni, nj))

        cnt += 1
                
t= int(input())

for tc in range(1, t+1):
    n, m, r, c, l= map(int, input().split())
    arr= [list(map(int, input().split())) for _ in range(n)]

    visited= [[0]*m for _ in range(n)]
    visited[r][c] = 1
    q = deque([(r, c)])

    solve(q)
    ans = 0
    for i in range(n):
        ans += visited[i].count(1)

    print(f"#{tc} {ans}")
