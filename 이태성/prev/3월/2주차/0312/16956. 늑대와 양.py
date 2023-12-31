import sys
from collections import deque
input = sys.stdin.readline

def is_valid(nr, nc):
    return 0 <= nr < R and 0 <= nc < C

def fence():
    for r, c in sheep:
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if is_valid(nr, nc) and pasture[nr][nc] == "W":
                return False
    return True

R, C = map(int, input().split())
pasture = []
sheep = deque()
for i in range(R):
    pasture.append(list(input()))
    for j in range(C):
        if pasture[i][j] == "S":
            sheep.append((i, j))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
# 4 방향에 늑대가 있는지 확인
if fence():
    print(1)
    for r in range(R):
        for c in range(C):
            if pasture[r][c] == ".":
                pasture[r][c] = "D"
    for line in pasture:
        print("".join(line))
else:
    print(0)
