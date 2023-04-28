from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def is_valid(nr, nc):
    return 0 <= nr < N and 0 <= nc < N

def bfs():
    cnt = 0
    q = deque()
    q.append((0, 0))
    V[0][0] = 0
    while q:
        r, c = q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if is_valid(nr, nc):
                tmp = 1
                if mapp[r][c] < mapp[nr][nc]:
                    tmp += mapp[nr][nc] - mapp[r][c]
                if V[nr][nc] > V[r][c] + tmp:
                    V[nr][nc] = V[r][c] + tmp
                    q.append((nr, nc))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mapp = [list(map(int, input().split())) for _ in range(N)]
    V = [[10000 for _ in range(N)] for _ in range(N)]
    bfs()
    print(f"#{tc} {V[N-1][N-1]}")