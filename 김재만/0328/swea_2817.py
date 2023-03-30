# 부분수열의 합
# 추가문제 20
import sys

sys.stdin = open('input.txt', 'r')


def comb(arr, n):
    global result

    for i in range(1 << n):
        ans_list = []
        for j in range(n):
            if i & (1 << j):
                ans_list.append(arr[j])

        if sum(ans_list) == k:
            result += 1


T = int(input())

for tc in range(1, T + 1):
    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    result = 0

    comb(A, n)
    print(f"#{tc} {result}")
