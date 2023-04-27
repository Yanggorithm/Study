t = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def solve(ci, cj, tmp):
    if len(tmp) == 7:
        result.add(tmp)
        return
    
    for d in range(4):
        ni, nj = ci + dx[d], cj + dy[d]
        if 0 <= ni < 4 and 0 <= nj < 4:
            solve(ni, nj, tmp+arr[ni][nj])
        

for tc in range(1, t+1):
    arr = [input().split() for _ in range(4)]

    result = set()
    for i in range(4):
        for j in range(4):
            solve(i, j, arr[i][j])
    print(f"#{tc} {len(result)}")