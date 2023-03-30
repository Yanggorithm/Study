# swea 실습 50
# 컨테이너 운반
import sys
sys.stdin = open('input.txt', 'r')


T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    wi = list(map(int, input().split()))
    ti = list(map(int, input().split()))

    wi = sorted(wi, reverse=True)
    ti = sorted(ti)

    ans = 0
    for t in range(m):
        for w in range(len(wi)):
            if ti[t] >= wi[w]:
                ans += wi[w]
                wi.pop(w)
                break

    print(f"#{tc} {ans}")
