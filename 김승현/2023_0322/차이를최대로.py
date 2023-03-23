N = int(input())
num_list = list(map(int, input().split()))

result = []
res = []
visited = [0] * N
def dfs(idx, cnt):
    if cnt == N:
        ans = 0
        for i in range(N - 1):
            ans += abs(result[i] - result[i + 1])
        res.append(ans)
        return

    for i in range(idx, N):
        if not visited[i]:
            result.append(num_list[i])
            visited[i] = 1
            dfs(idx, cnt + 1)
            visited[i] = 0
            result.pop()

dfs(0,0)
print(max(res))