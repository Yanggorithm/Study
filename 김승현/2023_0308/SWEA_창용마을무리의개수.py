import sys
sys.stdin = open('창용마을무리의개수.txt','r')

from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    visited = [1] + [0] * (N)

    people = [[] for _ in range(N + 1)]
    for i in range(M):
        start, end = map(int, input().split())

        people[start].append(end)
        people[end].append(start)

    cnt = 0
    for i in range(1, N):
        if not visited[i]:
            q = deque()
            q.append(i)
            visited[i] = 1

            while q:
                t = q.popleft()

                for j in people[t]:
                    if not visited[j]:
                        q.append(j)
                        visited[j] = 1

            cnt += 1

    ans = visited.count(0)
    print(f'#{test_case} {ans + cnt}')