import sys
from collections import deque

def is_valid(nr, nc):
    return 0 <= nr < N and 0 <= nc < M

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

input = sys.stdin.readline
N, M = map(int, input().split())
maze = []
jr, jc = 0, 0
fr, fc = 0, 0
for r in range(N):
    maze.append(input().strip())
    for c in range(M):
        if maze[r][c] == "J":
            jr, jc = r, c
        if maze[r][c] == "F":
            fr, fc = r, c
V = [[0 for _ in range(M)] for _ in range(N)]
q = deque()
q.append((jr, jc, 0))
V[jr][jc] = 1
exitttt = False
ans = 0
while q:
    r, c, tm = q.popleft()
    dis = abs(r - fr) + abs(c - fc)

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if not is_valid(nr, nc) and dis - tm >= 0:
            exitttt = True
            ans = tm+1
            break
        if is_valid(nr, nc) and V[nr][nc] == 0 and maze[nr][nc] == ".":
            q.append((nr, nc, tm+1))
            V[nr][nc] = 1

    if exitttt:
        print(ans)
        break
if not exitttt:
    print("IMPOSSIBLE")