from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def is_valid(nr, nc):
    return 0 <= nr < N and 0 <= nc < N

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    w_map = [list(map(int, input())) for _ in range(N)]
    V = [[2000 for _ in range(N)] for _ in range(N)]
    q = deque()
    q.append((0, 0))
    V[0][0] = 0
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if is_valid(nr, nc):
                if V[nr][nc] > V[r][c] + w_map[nr][nc]:
                    V[nr][nc] = V[r][c] + w_map[nr][nc]
                    q.append((nr, nc))

    print(f"#{tc} {V[N-1][N-1]}")