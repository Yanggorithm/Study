t = int(input())

def solve(i, tmp):
    global result
    if result <= tmp:
        return
    
    if i == n:
        result = min(result, tmp)
        return
    
    for k in range(n):
        if visited[k] == 0:
            visited[k] = 1
            solve(i+1, tmp + v[i][k])
            visited[k] = 0

    

for tc in range(1, t+1):
    n = int(input())
    v = [list(map(int, input().split())) for _ in range(n)]
    sumV = 0

    result = 9999999999
    visited = [0] * n
    solve(0, 0)
    print(f"#{tc} {result}")
