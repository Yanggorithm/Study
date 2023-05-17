def solve(i, sumV):
    global result
    if sumV <= result:
        return
    
    if i == n:
        result = max(result, sumV)
        return
    
    for j in range(n):
        if selected[j] == 0:
            selected[j] = 1
            solve(i+1, sumV * (p[i][j]/100))
            selected[j] = 0

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    p = [list(map(int, input().split())) for _ in range(n)]

    selected = [0] * n
    result = -1
    solve(0, 1)
    print(f"#{tc} {result*100:.6f}")