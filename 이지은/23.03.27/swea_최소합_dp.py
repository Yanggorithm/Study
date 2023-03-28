t = int(input())

for tc in range(1,t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    # 중간 위치까지의 합을 다시 계산하지 않도록 저장
    dp = [[0]*n for _ in range(n)]

    # 이동 방향이 왼쪽 => 오른쪽 or 위 => 아래
    for i in range(n):
        for j in range(n):
            # i, j 위치에서 위에서도 올 수 있고, 왼쪽에서도 올 수 있다.
            if i - 1 >= 0 and j - 1 >= 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1] + arr[i][j])
            # 위에서만 올 수 있다.
            elif i - 1 >= 0 and j - 1 < 0:
                dp[i][j] = dp[i-1][j] + arr[i][j]
            elif i - 1 < 0 and j - 1 >= 0:
                dp[i][j] = dp[i][j-1] + arr[i][j]
            elif i - 1 < 0 and j - 1 < 0:
                dp[i][j] = arr[i][j]
        
    print(f"#{tc} {dp[n-1][n-1]}")
