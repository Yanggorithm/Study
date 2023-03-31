# boj 14916
# 양고리즘 스터디 문제
# 거스름돈

n = int(input())

dp = [999999] * n
idx = n-1
dp[idx] = 0

while idx:
    dp