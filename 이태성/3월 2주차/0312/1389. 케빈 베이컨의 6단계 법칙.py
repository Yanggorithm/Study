import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
adjL = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    adjL[u].append(v)
    adjL[v].append(u)
min_kevin = 10000
min_idx = 0
for p in range(1, N+1):
    q = deque()
    q.append(p)
    visited = [0] * (N+1)
    visited[p] = 1
    nkb = 0
    while q:
        now = q.popleft()
        for np in adjL[now]:
            if visited[np] == 0:
                visited[np] = visited[now] + 1
                q.append(np)
                nkb += visited[np]
    if min_kevin > nkb:
        min_kevin = nkb
        min_idx = p
    elif min_kevin == nkb:
        if min_idx > p:
            min_idx = p
print(min_idx)