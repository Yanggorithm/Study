from collections import deque

N, M = map(int, input().split())

connect = [[] for _ in range(N + 1)]

for i in range(M):
    s, e = map(int, input().split())

    connect[s].append(e)
    connect[e].append(s)

cnt = 0
visited = [1] + [0] * N
cnt = 0
for i in range(1, N):
    if not visited[i]:
        q = deque()
        q.append(i)
        visited[i] = 1
        while q:
            t = q.popleft()
            for j in connect[t]:
                if not visited[j]:
                    q.append(j)
                    visited[j] = 1
        cnt += 1

ans = visited.count(0)

print(ans + cnt)