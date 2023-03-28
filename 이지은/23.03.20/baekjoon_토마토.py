import sys
from collections import deque

m, n = map(int, sys.stdin.readline().strip().split())
tomato = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

# 1: 익은 토마토, 0 : 익지 않은 토마토, -1: 없음

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

rotten = deque([])
notyet = []
nothing = []
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            rotten.append((i, j))

day = 0
def tomato_day():
    while rotten:
        ci, cj = rotten.popleft()  
        for d in range(4):
            ni, nj = ci+dx[d], cj+dy[d]
            if 0 <= ni < n and 0 <= nj < m and tomato[ni][nj] == 0:
                tomato[ni][nj] = tomato[ci][cj] + 1
                rotten.append((ni, nj))

def ans():
    global day
    for i in tomato:
        for j in i:
            if j == 0:
                print(-1)
                return
            elif day < j:
                day = j
    
    print(day-1)
    return

day = 0
tomato_day()
ans()
