def dfs(S):
    if S == 99:
        return
    for num in adjL[S]:
        if visited[num] == 0:
            visited[num] = 1
            dfs(num)

T = 10
for _ in range(1, T+1):
    tc, N = map(int, input().split())
    arr = list(map(int, input().split()))
    adjL = [[] for _ in range(100)]
    for i in range(N):
        u = arr[i*2]
        v = arr[i*2+1]
        adjL[u].append(v)
    visited = [0] * 100
    dfs(0)
    ans = visited[99]
    print(f"#{tc} {ans}")