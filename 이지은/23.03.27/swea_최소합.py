t = int(input())

dx = [0, 1]
dy = [1, 0]

def solve(now):
    global minV
    ci, cj = stack.pop()
    if (ci, cj) == (n-1, n-1):
        if minV > now:
            minV = now
        return
    
    for d in range(2):
        ni, nj = ci+dx[d], cj+dy[d]
        if 0 <= ni < n and 0 <= nj < n:
            stack.append((ni, nj))
            solve(now+arr[ni][nj])                
        
for tc in range(1,t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    stack = [(0,0)]
    minV = 9999999999
    solve(arr[0][0])
    print(f"#{tc} {minV}")