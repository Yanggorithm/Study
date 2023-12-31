def dfs(sub_sum, cnt):
    global min_cnt

    if cnt > min_cnt:
        return

    if sub_sum == M:
        min_cnt = min(min_cnt, cnt)
        return

    if sub_sum + 1 not in selected and 1 <= sub_sum + 1 <= 1000000:
        selected.add(sub_sum+1)
        dfs(sub_sum+1, cnt+1)

    if sub_sum * 2 not in selected and 1 <= sub_sum * 2 <= 1000000:
        selected.add(sub_sum*2)
        dfs(sub_sum*2, cnt+1)

    if sub_sum - 1 not in selected and 1 <= sub_sum - 1 <= 1000000:
        selected.add(sub_sum-1)
        dfs(sub_sum-1, cnt+1)

    if sub_sum - 10 not in selected and 1 <= sub_sum - 10 <= 1000000:
        selected.add(sub_sum-10)
        dfs(sub_sum-10, cnt+1)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    selected = set()
    selected.add(N)
    min_cnt = 10**9
    dfs(N, 0)
    print(f"#{tc} {min_cnt}")