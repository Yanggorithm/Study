# 동철이의 일 분배
# swea 과제 19
import sys
sys.stdin = open('input.txt', 'r')


def perm(sum_v, idx):
    global ans

    if sum_v <= ans:
        return

    if idx == n:
        ans = max(ans, sum_v)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            perm(sum_v * t_map[idx][i]/100, idx + 1)
            visited[i] = 0


T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    t_map = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    ans = 0
    perm_list = []
    perm(1, 0)
    ans *= 100
    print(f"#{tc} {ans:.6f}")
