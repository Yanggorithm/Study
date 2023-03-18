T = int(input())
for tc in range(1, T+1):
    N, S = map(int, input().split())
    numbers = sorted(list(map(int, input().split())))
    cnt = 0
    def dfs(idx, sub_sum, length):
        global cnt
        if idx == N:
            if sub_sum == S and length > 0:
                cnt += 1
            return
        if idx < N:
            dfs(idx+1, sub_sum+numbers[idx], length+1)
            dfs(idx+1, sub_sum, length)

    dfs(0, 0, 0)
    print(f"#{tc}", cnt)