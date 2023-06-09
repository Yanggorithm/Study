import sys
sys.stdin = open('거듭제곱.txt', 'r')

def check(cnt):
    global total

    if cnt == M:
        return

    total = total * N
    cnt += 1
    check(cnt)

for _ in range(10):
    test_case = int(input())

    total = 1
    N, M = map(int ,input().split())

    check(0)

    print(f'#{test_case} {total}')