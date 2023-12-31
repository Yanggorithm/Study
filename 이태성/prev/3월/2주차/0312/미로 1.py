from collections import deque
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def is_valid(nr, nc):
    return 0 <= nr < 16 and 0 <= nc < 16

def bfs(sr, sc, ar, ac):
    q = deque([(sr, sc)])
    visited = [[0] * 16 for _ in range(16)]
    visited[sr][sc] = 1
    while q:
        r, c = q.popleft()
        if (r, c) == (ar, ac):
            return 1
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if is_valid(nr, nc) and maze[nr][nc] != 1 and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                q.append((nr, nc))
    return 0

T = 10
for t_ in range(1, T+1):
    tc = f"#{int(input())}"
    maze = []
    search = 0
    sr = sc = ar = ac = 0
    for r in range(16):
        maze.append(list(map(int, input())))
        if search == 2:
            continue
        for c in range(16):
            if maze[r][c] == 2:
                sr, sc = r, c
                search += 1
            if maze[r][c] == 3:
                ar, ac = r, c
                search += 1
    print(tc, bfs(sr, sc, ar, ac))