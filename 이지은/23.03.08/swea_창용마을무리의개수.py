from collections import deque

t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

visited = [0] * (n+1)
q = deque([])
cnt = 0
for i in range(1, n+1):
    if visited[i] == 0:
        visited[i] = 1
        cnt += 1
    
    q.append(i)
    while q:
        c = q.popleft()
        for j in arr[c]:
            if visited[j] == 0:
                visited[j] = 1
                q.append(j)

print(f"#{tc} {cnt}")