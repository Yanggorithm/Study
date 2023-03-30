# swea 실습 53
# 이진탐색
import sys

sys.stdin = open('input.txt', 'r')


def search_bi(l, r, target, turn):
    global cnt

    m = (l + r) // 2

    if target == n_list[m]:
        cnt += 1
        return

    if l >= r:
        return

    if turn == 0:
        search_bi(l, m - 1, target, 1)
        search_bi(m + 1, r, target, 2)
    elif turn == 1:
        search_bi(m + 1, r, target, 2)
    else:
        search_bi(l, m - 1, target, 1)


T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    n_list = list(map(int, input().split()))
    m_list = list(map(int, input().split()))
    n_list.sort()
    cnt = 0

    for i in m_list:
        search_bi(0, n - 1, i, 0)

    print(f"#{tc} {cnt}")
