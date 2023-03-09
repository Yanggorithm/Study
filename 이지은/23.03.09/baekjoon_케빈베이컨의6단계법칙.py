import sys
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split())
friends = [[] * (n+1) for _ in range(n+1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    friends[a].append(b)
    friends[b].append(a)

for i in range(n+1):
    friends[i] = list(set(friends[i]))

kb = [[0] * (n+1) for _ in range(n+1)]
q = deque([])

for i in range(1, n+1):
    q.append(i)
    while q:
        ni = q.popleft()
        for j in friends[ni]:
            if kb[i][j] == 0:
                kb[i][j] = (kb[i][ni] + 1)
                q.append(j)

minV = n**m
ans = [0] * (n+1)
for i in range(1, n+1):
    ans[i] = sum(kb[i])
    
print(ans.index(min(ans[1:])))