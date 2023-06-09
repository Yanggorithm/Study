import heapq
import sys
sys.stdin = open('Shortest.txt', 'r')
input = sys.stdin.readline
INF = int(1e9)

T = int(input())

for test_case in range(1, T + 1):
    N, M, start, end = map(int, input().split())

    node = [[] for _ in range(N + 1)]

    for i in range(M):
        s, e, w = map(int, input().split())
        node[s].append([e, w])
        node[e].append([s, w])

    D = [INF] * (N + 1)

    def dijstra(start):
        q = []
        heapq.heappush(q, (0, start))
        D[start] = 0

        while q:
            dist, now = heapq.heappop(q)
            if dist > D[now]:
                continue

            for i in node[now]:
                cost = dist + i[1]
                if cost < D[i[0]]:
                    D[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

        return D

    ans = dijstra(start)
    print(f'#{test_case} {ans[end]}')
