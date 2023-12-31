import heapq
T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    distance = [float("inf") for _ in range(N+1)]
    distance[0] = 0
    node = [[] for _ in range(N+1)]
    V = [0 for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        node[s].append((e, w))
    q = []
    heapq.heappush(q, (0, 0))
    while q:
        tot_dis, idx = heapq.heappop(q)
        if V[idx]:
            continue
        V[idx] = 1
        for num, dis in node[idx]:
            if distance[num] > tot_dis + dis:
                distance[num] = tot_dis + dis
                heapq.heappush(q, (distance[num], num))
    print(f"#{tc} {distance[N]}")