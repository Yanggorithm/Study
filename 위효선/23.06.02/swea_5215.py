# SWEA_5215 햄버거 다이어트

# import sys
# sys.stdin = open("swea_5215.txt", "r")

def solution(n, u, sm):
    global utility

    if sm > K:
        return

    if n == N:
        utility = max(utility, u)
        return

    solution(n+1, u+scores[n], sm+kcals[n])
    solution(n+1, u, sm)


T = int(input())
for TC in range(1,T+1):
    N, K = map(int,input().split())

    scores = []
    kcals = []

    for _ in range(N):
        s, k = map(int,input().split())
        scores.append(s)
        kcals.append(k)

    utility = 0

    solution(0, 0, 0)
    print(f'#{TC} {utility}')