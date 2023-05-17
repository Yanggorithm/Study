def dfs(idx, sub_sum, pl, mi, di, mu, cnt):
    global maxV, minV

    if idx == N-1:
        maxV = max(maxV, sub_sum)
        minV = min(minV, sub_sum)
        return

    if cnt:
        if pl:
            dfs(idx+1, sub_sum+numbers[idx+1], pl-1, mi, di, mu, cnt-1)
        if mi:
            dfs(idx+1, sub_sum-numbers[idx+1], pl, mi-1, di, mu, cnt-1)
        if di:
            dfs(idx+1, sub_sum//numbers[idx+1], pl, mi, di-1, mu, cnt-1)
        if mu:
            dfs(idx+1, sub_sum*numbers[idx+1], pl, mi, di, mu-1, cnt-1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    calculator = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    minV = 100000001
    maxV = -1000000001
    dfs(-1, 0, calculator[0], calculator[1], calculator[3], calculator[2], N-1)
    print(f"#{tc}", maxV-minV)
    print("================")

