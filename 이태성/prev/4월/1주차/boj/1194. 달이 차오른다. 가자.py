import sys
from collections import deque
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def is_valid(nr, nc):
    return 0 <= nr < N and 0 <= nc < M

def bfs(sr, sc):
    global get_time

    q = deque()
    q.append((sr, sc, [0 for _ in range(6)], 0))
    V = [[0 for _ in range(M)] for _ in range(N)]
    V[sr][sc] = 0
    while q:
        r, c, key, length = q.popleft()
        if maze[r][c] == "1":
            return True
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if is_valid(nr, nc) and maze[nr][nc] != "#":
                # 문일 경우
                if 65 <= ord(maze[nr][nc]) <= 90:
                    if maze[nr][nc].lower() in key:
                        V[nr][nc] = V[r][c] + 1
                        q.append((nr, nc, key, length+1))
                        continue
                    else:
                        continue
                # 나머지 경우
                if 97 <= ord(maze[nr][nc]) <= 122:
                    key.append(maze[nr][nc])
                V[nr][nc] = V[r][c] + 1
                q.append((nr, nc, key, length+1))


    print(V)
    return False

N, M = map(int, input().split())
maze = []
sr = sc = 0
for r in range(N):
    maze.append(input().strip())
    for c in range(M):
        if maze[r][c] == "0":
            sr, sc = r, c
print(sr, sc)
print(maze)
get_time = 0
ans = -1
if bfs(sr, sc):
    ans = get_time
print(ans)

