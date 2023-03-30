# 특정한 최단 경로
import sys
import heapq
input = sys.stdin.readline


def dijkstra(start):
    visited = [INF] * (N+1)
    q = []
    heapq.heappush(q, (0, start))
    visited[start] = 0

    while q:
        dist, node = heapq.heappop(q)

        if visited[node] < dist:
            continue

        else:
            for n, d in adj_list[node]:
                sum_dist = dist+d
                
                if sum_dist < visited[n]:
                    visited[n] = sum_dist
                    heapq.heappush(q, (sum_dist, n))
    
    return visited


N, E = map(int, input().split())
INF = int(1e9)
visited = [INF] * (N+1)
adj_list = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    adj_list[a].append((b, c))
    adj_list[b].append((a, c))


v1, v2 = map(int, input().split())

ans1 = ans2 = 0
vi = dijkstra(1)
ans1 += vi[v1]
ans2 += vi[v2]
vi = dijkstra(v1)
ans1 += vi[v2]
ans2 += vi[N]
vi = dijkstra(v2)
ans1 += vi[N]
ans2 += vi[v1]

ans = min(ans1,ans2)
if ans >= INF:
    ans = -1
print(ans)
