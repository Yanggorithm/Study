import sys

sys.stdin = open("input(swea부분수열의합).txt", "r")


def dfs(n, sumV):
    global ans
    # 가지치기
    if K < sumV:
        return

    # 가능한 모든 경우 나열
    # 종료조건 꼭
    # 내가 가져오는 숫자 n이 문제에서 주어진 자연수 N개와 같아지면
    if n == N:
        # 그 합이 K와 같다 => 경우의 수 +1
        if sumV == K:
            ans += 1
        return

    # 재귀
    # 최소 1개의 수를 선택
    # 선택해서 사용하는경우
    dfs(n + 1, sumV + lst[n])
    # 사용하지 않는 경우
    dfs(n + 1, sumV)


T = int(input())
for tc in range(1, T + 1):
    # 자연수 N개, 합이 K가 되는 경우의 수 구하기
    N, K = map(int, input().split())

    # 수열 리스트
    lst = list(map(int, input().split()))

    # 경우의 수(전역변수로 체크)
    ans = 0

    # 자연수 0, 합 0부터 시작
    dfs(0, 0)

    print(f"#{tc} {ans}")
