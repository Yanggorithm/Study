def cal(a, b, op):
    if op == 0:
        return a+b
    elif op == 1:
        return a-b
    elif op == 2:
        return a*b
    elif op == 3:
        return int(a/b)

def solve(i, result):
    global maxV, minV
    if i == n:
        if minV > result:
            minV = result
        if maxV < result:
            maxV = result
        return
    
    for j in range(4):
        if op[j]:
            op[j] -= 1
            solve(i+1, cal(result, num[i], j))
            op[j] += 1

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    op = list(map(int, input().split()))
    num = list(map(int, input().split()))
    
    maxV = -99999999
    minV = 99999999
    solve(1, num[0])

    print(f"#{tc} {maxV - minV}")