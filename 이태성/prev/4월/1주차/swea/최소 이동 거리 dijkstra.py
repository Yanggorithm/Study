def dijkstra(S):
    for _ in range(N+1):
        minI = -1
        minV = float("inf")

        for i in range(N+1):
            if V[i] == 0 and distance[i] < minV:
                minI = i
                minV = distance[i]

        V[minI] = 1
        for i in range(N+1):
            if adjM[minI][i] and V[i] == 0:
                distance[i] = min(distance[i], distance[minI]+adjM[minI][i])

T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    adjM = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        adjM[s][e] = w

    V = [0 for _ in range(N+1)]
    distance = [float("inf") for _ in range(N+1)]
    distance[0] = 0
    dijkstra(0)

    print(f"#{tc} {distance[N]}")