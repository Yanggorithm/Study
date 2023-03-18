import sys

sys.stdin = open("input(baek부분수열의합).txt", "r")


def dfs(n, sumV, cnt):
    global ans
    if n == N:
        if sumV == S and cnt > 0:
            ans += 1
        return

    # 하부함수 호출
    dfs(n + 1, sumV + lst[n], cnt + 1)
    dfs(n + 1, sumV, cnt)


N, S = map(int, input().split())
lst = list(map(int, input().split()))
ans = 0
dfs(0, 0, 0)
print(ans)
