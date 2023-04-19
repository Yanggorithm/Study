import sys
from collections import deque
input = sys.stdin.readline

start, end = map(int, input().split())

visited = [0 for _ in range(100001)]
visited[start] = 1

q = deque()
q.append(start)

while q:
    check = q.popleft()

    if check == end:
        print(visited[check] - 1)
        break

    for i in (check * 2, check - 1, check + 1):
        if 0 <= i < 100001 and not visited[i]:
            if i == check * 2:
                q.appendleft(i)
                visited[i] = visited[check]
            else:
                q.append(i)
                visited[i] = visited[check] + 1