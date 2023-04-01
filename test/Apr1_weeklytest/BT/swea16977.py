# 실습 55
# 전기버스 2

def electronic_bus(n, battery):
    pass


# dp 로 풀면 더 쉽겠는데 ?

T = int(input())

for tc in range(1, T + 1):
    n, *n_list = map(int, input().split())

    dp = [99999] * n
    cnt = 0
    dp[0] = 0

    for i in range(len(n_list)):
        for j in range(n_list[i]):
            cnt = dp[i] + 1
            if i+j+1 < n:
                dp[i + j + 1] = min(dp[i + j + 1], cnt)

    print(f'#{tc} {dp[-1] - 1}')
