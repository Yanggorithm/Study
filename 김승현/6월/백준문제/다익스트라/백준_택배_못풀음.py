import sys
import heapq

input = sys.stdin.readline

inf = int(1e10)
V, E = map(int, input().split())

# 시작점과 끝점간의 가중치를 나타냄
node = [[] for _ in range(V + 1)]



for i in range(E):
    s, e, w = map(int, input().split())
    node[s].append([e, w])
    node[e].append([s, w])

def djkstra(start):
    q = []
    D = [inf] * (V + 1)
    D[start] = 0
    move = [[] for _ in range(V + 1)]

    heapq.heappush(q, [0, start])

    while q:
        dist, now = heapq.heappop(q)

        if dist > D[now]:
            continue

        for i in node[now]:
            cost = dist + i[1]

            if cost < D[i[0]]:
                D[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

                if i[0] not in move:
                    move[now].append(i[0])

    return D

for i in range(1, V + 1):
    res = djkstra(i)
    print(res)
    # res[i - 1] = '-'