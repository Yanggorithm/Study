import sys
from collections import deque
input = sys.stdin.readline

def dfs(start):
    global min_cs
    if len(stack) == M:
        # 여기서 계산
        min_cs = min(min_cs, distance(stack))
        return
    for i in range(start, len(chicken)):
        if chicken[i] not in stack:
            stack.append(chicken[i])
            dfs(i+1)
            stack.pop()

def distance(stack):
    tot = 0
    for r, c in home:
        min_dis = 1000000000000
        for p, q in stack:
            min_dis = min(min_dis, abs(r-p)+abs(c-q))
        tot += min_dis
    return tot

N, M = map(int, input().split())
# 0은 빈 칸, 1은 집, 2는 치킨집
# 1 <= 집의 개수 <= 2N
# 1 <= 치킨집의 개수 <= 13

# 치킨집과 집을 따로 받는다.
chicken = deque()
home = deque()
ground = []
# 전체 지도 받기
for r in range(N):
    ground.append(list(map(int, input().split())))
    for c in range(N):
        if ground[r][c] == 0:
            continue
        if ground[r][c] == 1:
            home.append((r, c))
        elif ground[r][c] == 2:
            chicken.append((r, c))
stack = []
min_cs = 1000000000000
# 치킨 집을 골라야 한다.
# 없애야 할 치킨 집을 고르고
# 결국 없앨 치킨집을 고르는 순열을 만들어야 한다.

dfs(0)
print(min_cs)