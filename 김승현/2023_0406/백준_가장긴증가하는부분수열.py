N = int(input())
n_list = list(map(int, input().split()))

dp = [1 for i in range(N)]
result = 0

for i in range(N):
    for j in range(i):
        if n_list[i] > n_list[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))