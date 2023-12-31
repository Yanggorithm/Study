import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    dp = [[0 for _ in range(N)] for _ in range(2)]
    sticker = [list(map(int, input().split())) for _ in range(2)]

    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]

    if N > 1:
        dp[0][1] = sticker[0][1] + dp[1][0]
        dp[1][1] = sticker[1][1] + dp[0][0]
    if N > 2:
        for i in range(2, N):
            dp[0][i] = max(dp[1][i-2], dp[1][i-1]) + sticker[0][i]
            dp[1][i] = max(dp[0][i-2], dp[0][i-1]) + sticker[1][i]
    print(max(dp[0][N-1], dp[1][N-1]))
