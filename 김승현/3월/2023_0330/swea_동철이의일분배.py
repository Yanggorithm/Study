# 직원들 번호 1 부터 N
# 해야할 일 번호 1 부터 N
# i번 직원이 j번일을 하면 성공할확률 P_i,j
# 주어진 일이 모두 성공할 확률의 최댓값
import sys
sys.stdin = open('동철이의일분배.txt', 'r')

def check(cnt, result):
    global max_v
    if cnt == N:
        max_v = max(result, max_v)
        return

    if cnt >= 1:
        if max_v > result:
            return

    for i in range(N):
        if not visited[i] and n_list[cnt][i] != 0:
            visited[i] = 1
            result *= (n_list[cnt][i] / 100)
            check(cnt + 1, result)
            result /= (n_list[cnt][i] / 100)
            visited[i] = 0

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    n_list= [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    max_v = 0
    check(0, 1)
    ans = max_v * 100
    print(f'#{test_case} {ans:.6f}')