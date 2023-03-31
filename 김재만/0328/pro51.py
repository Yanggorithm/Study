# swea 실습 51
# 16904. 화물 도크
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    time_table = []
    for _ in range(n):
        s, e = map(int, input().split())
        time_table.append([s, e])

    time_table.sort(key=lambda x: x[1])

    ans = 0
    start = 0
    end = 0
    for i in range(n):
        n_start = time_table[i][0]
        if end <= n_start:
            ans += 1
            end = time_table[i][1]

    print(f"#{tc} {ans}")
