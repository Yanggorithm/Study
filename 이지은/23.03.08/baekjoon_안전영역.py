# 1. 높이별로 물에 잠기지 않는 영역을 구한다
# 2. 연결된 영역을 표시한다
# 3. 표시된 영역의 개수를 구한다

import sys
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n = int(sys.stdin.readline().strip())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

tmp = []

for i in range(n):
    for j in range(n):
        tmp.append((i, j))

visited = [[0]*n for _ in range(n)]
q = deque([])
mx = 1

for h in range(101):
    tmp2 = []
    # h보다 높은 지점 높은 지점 찾기
    for ci, cj in tmp:
        # 높이 h이하인 지점 지우기
        if arr[ci][cj] <= h:
            visited[ci][cj] = -1
        else:
            visited[ci][cj] = 0
            tmp2.append((ci, cj))
    
    tmp = tmp2    
    if len(tmp) == 0:
        break

    cnt = 0
    for i, j in tmp:
        if visited[i][j] == 0:
            cnt += 1
            visited[i][j] = cnt
            q.append((i, j))

            while q:
                ci, cj = q.popleft()
                for d in range(4):
                    ni, nj = ci+dx[d], cj + dy[d]
                    if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0 and arr[ni][nj] > h:
                        q.append((ni, nj))
                        visited[ni][nj] = cnt    

    if cnt > mx:
        mx = cnt

print(mx)
