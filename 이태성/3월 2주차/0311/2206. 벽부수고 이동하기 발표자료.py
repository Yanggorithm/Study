import sys
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def is_valid(nr, nc):
    return 0 <= nr < N and 0 <= nc < M

input = sys.stdin.readline
N, M = map(int, input().split())
route = [list(map(int, input().strip())) for _ in range(N)]
q = deque()
q.append((0, 0, True))
visited_True = [[0] * M for _ in range(N)]
visited_False = [[0] * M for _ in range(N)]
visited_True[0][0] = 1
visited_False[0][0] = 1
while q:
    r, c, crush = q.popleft()
    if (r, c) == (N-1, M-1):
        break
    if crush:
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if is_valid(nr, nc) and visited_True[nr][nc] == 0:
                visited_True[nr][nc] = visited_True[r][c] + 1
                if route[nr][nc] == 1:
                    q.append((nr, nc, False))
                    visited_False[nr][nc] = visited_True[r][c] + 1
                else:
                    q.append((nr, nc, True))
    else:
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if is_valid(nr, nc) and visited_False[nr][nc] == 0 and route[nr][nc] == 0:
                visited_False[nr][nc] = visited_False[r][c] + 1
                q.append((nr, nc, False))

ans = max(visited_True[N-1][M-1], visited_False[N-1][M-1])
if ans:
    print(ans)
else:
    print(-1)
