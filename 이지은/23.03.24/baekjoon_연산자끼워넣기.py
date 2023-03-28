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

import sys

n = int(sys.stdin.readline().strip())
num = list(map(int, sys.stdin.readline().strip().split()))
op = list(map(int, sys.stdin.readline().strip().split()))
    
maxV = -9999999999
minV = 9999999999
solve(1, num[0])

print(maxV)
print(minV)