# boj 14916
# 양고리즘 스터디 문제
# 거스름돈

n = int(input())

dp = [999999] * (n+1)
dp[0] = 0

for i in range(2,n+1):
    if i-2 >= 0:
        dp[i] = min(dp[i], dp[i-2] + 1)
    if i-5 >= 0:
        dp[i] = min(dp[i], dp[i-5] + 1)

if dp[n] != 999999:
    print(dp[n])
else:
    print(-1)
