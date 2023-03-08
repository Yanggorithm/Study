# 42%에서 오답
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split())
if m == 0:
    print(0)
else:
    arr = [[] for _ in range(1001)]

    for i in range(m):
        u, v = map(int, sys.stdin.readline().strip().split())
        arr[u].append(v)
        arr[v].append(u)

    si = 0
    visited = [0] * 1001
    cnt = 0

    for o in range(1, 1001):
        if arr[o] and visited[o] == 0:
            cnt += 1
            visited[o] = cnt
            q = deque([o])

            while q:
                ni = q.popleft()
                for j in arr[ni]:
                    if visited[j] == 0:
                        visited[j] = cnt
                        q.append(j)

    node = [0] * (m+1)
    for i in range(1, 1001):
        if visited[i]:
            node[visited[i]] += 1
    c = sum(node)
    
    print(n - c + 1 if c < n else max(visited))
