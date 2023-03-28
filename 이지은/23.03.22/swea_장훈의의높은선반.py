def solve(i):
    global minV
    if sum(tmp) >= b and sum(tmp)-b < minV:
        minV = sum(tmp) - b
        return
    
    if i == n:
        return
    
    
    
    for j in range(i, n):
        tmp.append(height[j])
        solve(j+1)
        tmp.pop()

t = int(input())

for tc in range(1,t+1):
    n, b = map(int, input().split())
    height = list(map(int, input().split()))
    s = sum(height)

    tmp = []
    minV = 10000*n
    solve(0)
    print(f"#{tc} {minV}")
