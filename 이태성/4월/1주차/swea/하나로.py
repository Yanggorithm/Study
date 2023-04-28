def dfs(idx, sr, sc, sub_sum):
    global minV
    if idx == N-1:
        minV = min(minV, sub_sum)
        return
    for i in range(1, N):
        r, c = island[i]
        if V[i] == 0:
            V[i] = 1
            dfs(idx+1, r, c, sub_sum+(abs(sr-r)+abs(sc-c))**2)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    island = []
    x_dir = list(map(int, input().split()))
    y_dir = list(map(int, input().split()))
    for i in range(N):
        island.append((x_dir[i], y_dir[i]))
    E = float(input())
    minV = 10**9
    V = [0] * N
    dfs(0, x_dir[0], y_dir[0], 0)
    print(minV)