import sys
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def is_valid(r, c):
    return 0 <= r < N and 0 <= c < M

input = sys.stdin.readline
N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]

def bfs(sr, sc):
    q = deque()
    q.append((sr, sc, 1, paper[sr][sc], [(sr, sc)]))
    maxSum = 0
    while q:
        r, c, length, total, V = q.popleft()
        if length == 4:
            if maxSum < total:
                maxSum = total
        if length <= 3:
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if is_valid(nr, nc) and (nr, nc) not in V:
                    q.append((nr, nc, length + 1, total + paper[nr][nc], V + [(nr, nc)]))
    return maxSum

f_model = [[(0, 0), (1, 0), (1, -1), (1, 1)], [(0, 0), (0, 1), (1, 1), (0, 2)], [(0, 0), (1, 0), (2, 0), (1, 1)],
           [(0, 0), (1, 0), (2, 0), (1, -1)]]

lastMax = 0
for r in range(N):
    for c in range(M):
        now_max = bfs(r, c)

        for i in f_model:
            now = 0
            for p, q in i:
                nr = r + p
                nc = c + q
                if is_valid(nr, nc):
                    now += paper[nr][nc]
            if now > now_max:
                now_max = now
        if lastMax < now_max:
            lastMax = now_max

print(lastMax)
