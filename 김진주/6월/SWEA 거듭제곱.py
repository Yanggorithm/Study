import sys
sys.stdin = open('input.txt', 'r')

T = 10
for _ in range(1, T+1):
    TC = int(input())
    N, M = map(int, input().split())

    def gop(N, M) :
        if M == 0 :
            return 1
        else:
            return N * gop(N, M-1)

    print(f'#{TC} {gop(N, M)}')