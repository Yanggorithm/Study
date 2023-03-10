import sys

def solve(i, cnt):
    global ans
    if i == n:
        return

    if cnt == n//2:
        start = 0
        link = 0
        for x in range(n):
            for y in range(n):
                if selected[x] and selected[y]:
                    start += arr[x][y]
                elif selected[x] == 0 and selected[y] == 0:
                    link += arr[x][y]
        ans.append(abs(start-link))
        return
    
    for j in range(n):
        if selected[j] == 0:
            selected[j] = 1
            solve(i+1, cnt+1)
            selected[j] = 0

n = int(sys.stdin.readline().strip())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

selected = [0] * n
ans = []
solve(0, 0)

print(min(ans))
