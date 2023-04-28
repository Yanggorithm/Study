import sys
from collections import deque
input = sys.stdin.readline

def is_valid(nr, nc):
    return 0 <= nr < N and 0 <= nc < N

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(sr, sc):
    global ans
    q = deque([(sr, sc)])
    # 마지막에 grape의 값을 바꿔줄 리스트
    merge = [(sr, sc)]
    sum_merge = grape[sr][sc]
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if is_valid(nr, nc) and L <= abs(grape[r][c] - grape[nr][nc]) <= R and V[nr][nc] == 0:
                V[nr][nc] = 1
                q.append((nr, nc))
                merge.append((nr, nc))
                sum_merge += grape[nr][nc]

    if len(merge) > 1:
        ans += 1
        avg = int(sum_merge / len(merge))
        for xr, xc in merge:
            grape[xr][xc] = avg


N, L, R = map(int, input().split())
grape = [list(map(int, input().split())) for _ in range(N)]

# 값이 범위 안에 있으면 연결 해주는 함수.
# 연결 이후에 값을 바꿔주는 함수
# 인구 이동이 있었는지 확인하는 함수.
time = 0
while True:
    V = [[0 for _ in range(N)] for _ in range(N)]

    ans = 0
    for sr in range(N):
        for sc in range(N):
            if V[sr][sc]:
                continue
            V[sr][sc] = 1
            bfs(sr, sc)
    if ans == 0:
        break
    else:
        time += 1

print(time)