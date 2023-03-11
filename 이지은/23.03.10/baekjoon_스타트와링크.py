import sys

def solve(i, cnt):
    global ans
    
    if cnt == n//2:
        start = 0
        link = 0
        for x in range(n):
            for y in range(n):
                if x==y:continue
                elif selected[x] and selected[y]:
                    start += arr[x][y]
                elif selected[x] == 0 and selected[y] == 0:
                    link += arr[x][y]
        ans = min(ans, abs(start-link))
        return
    
    for j in range(i, n):
        if selected[j] == 0:
            selected[j] = 1
            solve(j+1, cnt+1)
            selected[j] = 0

n = int(sys.stdin.readline().strip())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

selected = [0] * n
ans = 9**n*2
solve(0, 0)

print(ans)