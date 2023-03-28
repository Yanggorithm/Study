import sys

n = int(sys.stdin.readline().strip())
arr = [[0]*n for _ in range(n)]
def nqueen(row, cnt):
    global ans
    if cnt == n:
        ans += 1
        return
    
    # 열
    for i in range(n):
        possible = True
        
        # 행
        for j in range(row):
            if arr[j][i]:
                possible = False
                break
        
        # 대각선
        for j in range(1, row+1):
            if i - j >= 0 and row - j >= 0 and arr[row-j][i-j]:
                possible = False
                break
            if i + j < n and row - j >= 0 and arr[row-j][i+j]:
                possible = False
                break
        
        if possible:
            arr[row][i] = 1
            nqueen(row+1, cnt+1)
            arr[row][i] = 0      

ans = 0
visited = []
nqueen(0, 0)
print(ans)