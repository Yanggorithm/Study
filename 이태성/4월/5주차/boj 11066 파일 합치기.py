import sys

input = sys.stdin.readline

for _ in range(int(input())):
    K = int(input())
    files = list(map(int, input().split()))
    min_cost = [[0] * K for _ in range(K)]  # 메모이제이션 리스트

    # 연속합
    sub_sum = [0]
    for idx in range(K):
        sub_sum.append(sub_sum[-1] + files[idx])

    # size 크기로 묶은 그룹들의 min_cost 구하기
    for size in range(1, K):
        for start in range(K - size):
            end = start + size

            result = float('inf')
            for cut in range(start, end):
                result = min(result, min_cost[start][cut] + min_cost[cut + 1][end] + sub_sum[end + 1] - sub_sum[start])

            min_cost[start][end] = result

    print(min_cost[0][K - 1])