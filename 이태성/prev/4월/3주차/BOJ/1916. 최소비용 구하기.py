import sys
import heapq
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

def dijkstra(start, graph, dist):
    heap = []
    heapq.heappush(heap, (0, start))
    dist[start] = 0
    while heap:
        d, now = heapq.heappop(heap)
        if dist[now] < d:
            continue
        for i in graph[now]:
            cost = d + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))

# 입력 받기
n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
start, end = map(int, input().split())

# 최단 경로 계산
dist = [INF] * (n + 1)
dijkstra(start, graph, dist)

# 출력
print(dist[end])
