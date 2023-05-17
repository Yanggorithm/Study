import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    V = [0] * (N+1)
    application = deque(sorted([list(map(int, input().split())) for _ in range(M)], key=lambda x: x[1]))
    cnt = 0
    while application:
        ai, bi = application.popleft()

        for i in range(ai, bi+1):
            if V[i]:
                continue
            cnt += 1
            V[i] = 1
            break
    print(cnt)
