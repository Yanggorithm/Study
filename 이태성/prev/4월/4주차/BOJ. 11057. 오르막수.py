from pprint import pprint
n = int(input())
dp = [[0 for _ in range(10)] for _ in range(n+1)]

# 길이가 1인 오르막 수 초기화
for i in range(10):
    dp[1][i] = 1

# 길이가 2 이상인 오르막 수 개수 구하기
for i in range(2, n+1):
    for j in range(10):
        for k in range(j+1):
            dp[i][j] += dp[i-1][k]
            dp[i][j] %= 10007

# 길이가 n인 오르막 수의 총 개수 구하기
answer = sum(dp[n]) % 10007
print(answer)
pprint(dp)