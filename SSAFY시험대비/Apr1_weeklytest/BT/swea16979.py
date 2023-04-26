# 실습 55
# 최소 생산 비용
import sys

sys.stdin = open('input.txt', 'r')


# 순열을 구한다.
def perm(m, cnt):
    global result

    # 가지치기
    if cnt > result:
        return

    if n == m:
        result = min(result, cnt)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            perm(m+1, cnt+vij[m][i])
            visited[i] = 0


T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    vij = [list(map(int, input().split())) for _ in range(n)]

    visited = [0] * n
    result = 9999999999
    perm(0, 0)
    print(f'#{tc} {result}')
