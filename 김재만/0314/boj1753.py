# 최단경로
# dijkstra 문제
import heapq
import sys
input = sys.stdin.readline


def dijkstra(start):

    heap = []
    # 시작 노드 거리는 당연히 0
    heapq.heappush(heap,(0,start))
    visited[start] = 0

    while heap:
        dist, node = heapq.heappop(heap)

        if visited[node] < dist:
            continue

        for d,n in adj_list[node]:
            sum_dist = dist + d

            if sum_dist < visited[n]:
                visited[n] = sum_dist
                heapq.heappush(heap, (sum_dist, n))


V, E = map(int, input().split())
k = int(input())
INF = int(1e9)
visited = [INF] * (V+1)
adj_list = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int,input().split())
    adj_list[u].append((w,v))

dijkstra(k)

for i in range(1,V+1):
    if visited[i] != INF:
        print(visited[i])
    else:
        print("INF")