import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
def dfs(S):
    global cnt
    if S == N:
        return
    for num in adjL[S]:
        if visited[num] == 0:
            visited[num] = 1
            dfs(num)

N, M = map(int, input().split())
adjL = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    adjL[u].append(v)
    adjL[v].append(u)
visited = [0] * (N+1)
cnt = 0
for num in range(1, N+1):
    if visited[num] == 0:
        dfs(num)
        cnt += 1
print(cnt)