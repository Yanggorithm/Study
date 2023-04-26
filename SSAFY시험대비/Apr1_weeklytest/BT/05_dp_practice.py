# 개미전사

n = 4
n_list = [1,3,1,5]

dp = [0] * n

dp[0] = n_list[0]
dp[1] = max(n_list[0], n_list[1])
for i in range(2,n):
    dp[i] = max(dp[i-1], n_list[i]+dp[i-2])

print(dp)

# 1로 만들기

x = 26
dp = [0] * (x+1)

for i in range(2, x+1):
    dp[i] = dp[i-1] + 1
    
    if i % 2 == 0:
        dp[i] = min(dp[i],dp[i//2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i],dp[i//3] + 1)
    if i % 5 == 0:
        dp[i] = min(dp[i],dp[i//5] + 1)

print(dp)