from collections import deque
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ground = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    distance = [[0] * N for _ in range(N)]
    q = deque()
    q.append((0, 0))
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if nr == 0 and nc == 0:
                    continue
                elif visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    distance[nr][nc] = distance[r][c] + ground[nr][nc]
                    q.append((nr, nc))
                else:
                    if distance[nr][nc] > ground[nr][nc] + distance[r][c]:
                        distance[nr][nc] = distance[r][c] + ground[nr][nc]
                        q.append((nr, nc))

    print(f"#{tc}", distance[-1][-1])