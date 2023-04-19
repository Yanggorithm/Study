from collections import deque

N = int(input())

First, End = map(int, input().split())

E = int(input())

people = [[] for _ in range(N + 1)]

for i in range(E):
    s, e = map(int, input().split())

    people[s].append(e)
    people[e].append(s)

visited = [0] * (N + 1)
q = deque()
q.append(First)
visited[First] = 1

while q:
    t = q.popleft()

    for i in people[t]:
        if not visited[i]:
            q.append(i)
            visited[i] = visited[t] + 1

if visited[End]:
    print(visited[End] - 1)
else:
    print(-1)
