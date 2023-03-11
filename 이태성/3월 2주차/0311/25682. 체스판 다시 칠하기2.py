import sys
input = sys.stdin.readline

def paint(color):
    dp = [[0] * (M+1) for _ in range(N+1)]
    for r in range(N):
        for c in range(M):
            if (r+c) % 2 == 0:
                value = board[r][c] != color
            else:
                value = board[r][c] == color
            dp[r+1][c+1] = dp[r][c+1] + dp[r+1][c] - dp[r][c] + value
    count = int(1e9)
    for r in range(1, N-K+2):
        for c in range(1, M-K+2):
            count = min(count,dp[r+K-1][c+K-1] - dp[r+K-1][c-1] - dp[r-1][c+K-1] + dp[r-1][c-1])
    return count

N,M,K = map(int,input().split())
board = [list(input().strip()) for _ in range(N)]
print(min(paint('W') , paint('B')))