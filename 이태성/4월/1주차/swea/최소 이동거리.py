def dfs(s, distance):
    global minD
    if minD <= distance:
        return

    if s == N:
        minD = min(minD, distance)
        return

    for v, w in adjM[s]:
        if V[v] == 0:
            V[v] = 1
            dfs(v, distance+w)
            V[v] = 0

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    adjM = [[] for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        adjM[s].append((e, w))
    V = [0 for _ in range(N+1)]
    minD = 10**13
    dfs(0, 0)
    print(f"#{tc} {minD}")