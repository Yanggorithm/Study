import sys
sys.stdin = open("input(twonumbers).txt", "r")

T = int(input())
for tc in range(1, T+1):
    n, m = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    if n <= m:
        n, m = n, m
        A, B = A, B
    else:
        n, m = m, n
        A, B = B, A

    maxx = 0
    for i in range(m-n+1):
        summ = 0
        for j in range(n):
            summ += A[j] * B[i+j]
        if maxx < summ:
            maxx = summ

    print(f'#{tc} {maxx}')






