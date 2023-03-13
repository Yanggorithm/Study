import sys
from collections import deque
input = sys.stdin.readline
def bfs(X):
    visited[X] = 0
    q = deque()
    q.append(X)
    while q:
        nc = q.popleft()
        for city in adjL[nc]:
            if visited[city] == -1:
                visited[city] = visited[nc] + 1
                q.append(city)
                if visited[city] == K:
                    result.append(city)
N, M, K, X = map(int, input().split())
adjL = [[] for _ in range(N+1)]
visited = [-1] * (N+1)
for _ in range(M):
    u, v = map(int, input().split())
    adjL[u].append(v)
result = []
bfs(X)
if result:
    result.sort()
    for city in result:
        print(city)
else:
    print(-1)