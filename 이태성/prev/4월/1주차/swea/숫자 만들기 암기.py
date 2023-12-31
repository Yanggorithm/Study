def dfs(idx, nowV):
    if idx >= N - 1:
        global minV, maxV
        maxV = max(maxV, nowV)
        minV = min(minV, nowV)
        return
    for i in range(4):
        if calculator[i]:
            calculator[i] -= 1
            dfs(idx+1, cal(nowV, numbers[idx+1], i))
            calculator[i] += 1

def cal(nowV, number_i, i):
    if i == 0:
        return nowV + number_i
    elif i == 1:
        return nowV - number_i
    elif i == 2:
        return nowV * number_i
    else:
        return int(nowV/number_i)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    calculator = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    minV = 10**9
    maxV = -(10**9)
    dfs(0, numbers[0])
    print(f"#{tc} {maxV-minV}")