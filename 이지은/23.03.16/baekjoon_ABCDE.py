import sys
from collections import deque

# 5개 이상의 일렬로 나타낼 수 있는 노드 개수
def solve(q, cnt):
    global ans
    if ans:
        return
    
    if cnt == 4:
        ans = 1
        return
    
    while q:
        c = q.popleft()
        for i in friends[c]:
            if ans:
                return
            
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1
                solve(q, cnt+1)
                visited[i] = 0

n, m = map(int, sys.stdin.readline().strip().split())
friends = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    friends[a].append(b)
    friends[b].append(a)

visited = [0] * n
ans = 0
for i in range(n):
    visited[i] = 1
    solve(deque([i]), 0)
    visited[i] = 0

print(ans)
