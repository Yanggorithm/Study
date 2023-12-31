import sys
from collections import deque
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def is_valid(nr, nc):
    return 0 <= nr < N and 0 <= nc < M

def bfs(sr, sc):
    V = [[0 for _ in range(M)] for _ in range(N)]
    q = deque([(sr, sc)])
    V[sr][sc] = 1
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if is_valid(nr, nc):
                if building[nr][nc] != "#" and V[nr][nc] == 0:
                    V[nr][nc] = V[r][c] + 1
                    q.append((nr, nc))
            else:
                # 탈출 했기 때문에 시간을 리턴
                return V[r][c]
    return 0
T = int(input())
for tc in range(1, T+1):
    M, N = map(int, input().split())
    sr = sc = 0
    fire = []
    building = []
    for r in range(N):
        building.append(input().strip())
        for c in range(M):
            if building[r][c] == "@":
                sr, sc = r, c
            elif building[r][c] == "*":
                fire.append((r, c))
    fire_time = 99999
    sang_time = bfs(sr, sc)
    for fr, fc in fire:
        if fire_time <= sang_time:
            break
        fire_time = min(bfs(fr, fc), fire_time)

    if 0 < sang_time < fire_time:
        print(sang_time)
    else:
        print("IMPOSSIBLE")