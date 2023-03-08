from collections import deque
import sys

n, m, k, x = map(int, sys.stdin.readline().strip().split())
arr = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    arr[a].append(b)

distance = [-1] * (n+1)
q= deque([x])
distance[x] = 0

while q:
    ni = q.popleft()
    for i in arr[ni]:
        if distance[i] == -1:
            distance[i] = (distance[ni] + 1)
            q.append(i)
        
result = []
for i in range(1, n+1):
    if distance[i] == k:
        result.append(i)

if result:
    print("\n".join(map(str, result)))
else:
    print(-1)
