'''
크기 n 인 정수 삼각형
맨 위층부터 시작해서 바로 아래 숫자 중 하나를 선택하면서 내려온다.
선택된 수의 합이 최대가 되는 경로 구하기
경우 3가지 : idx=0, n, 나머지
'''

n = int(input())
dp = []
for _ in range(n):
    dp.append(list(map(int, input().split())))

k = 2 # (세번째 줄 인덱스 범위) == (i+1)
for i in range(1, n): # (두번째 줄) 1부터 시작
    for j in range(k):
        # 바로 위층 값 가져와서 아래층 값에 더하기
        if j == 0:
            dp[i][j] += dp[i - 1][j]
            # dp[i][j] = dp[i-1][j] + dp[i][j]
        # 왼쪽 대각선 위층 값 가져와서 아래층 값에 더하기
        elif i == j:
            dp[i][j] += dp[i - 1][j - 1]
            # dp[i][j] = dp[i-1][j-1] + dp[i][j]
        # (바로 위층 vs 왼쪽 대각선 위층) 큰 값을 아래층 값에 더하기
        else:
            dp[i][j] += max(dp[i - 1][j - 1], dp[i - 1][j])

    # 아래층이 한 칸 더 많기 때문에 +1
    k += 1
# 맨 아래층 값 중 가장 큰 값 출력
print(max(dp[n-1]))