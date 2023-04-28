import heapq

def dijkstra(graph, start):
    n = len(graph)
    INF = int(1e9)
    distance = [INF] * n
    visited = [False] * n
    distance[start] = 0
    q = [(0, start)]

    while q:
        dist, now = heapq.heappop(q)

        if visited[now]:
            continue
        visited[now] = True

        for v, w in graph[now]:
            cost = dist + w
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(q, (cost, v))

    return distance
