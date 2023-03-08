dx = [-1,1,0,0]
dy = [0,0,-1,1]

for tc in range(1, 11):
    t = int(input())
    arr = [input() for _ in range(16)]

    si, sj, ei, ej = 0, 0, 0, 0
    for i in range(16):
        for j in range(16):
            if arr[i][j] == "2":
                si, sj = i, j
            elif arr[i][j] == "3":
                ei, ej = i, j
    
    stack = [(si,sj)]
    visited = [[0] * 16 for _ in range(16)]
    visited[si][sj] = 1

    while stack:
        ci, cj = stack.pop()
        for d in range(4):
            ni, nj = ci+dx[d], cj+dy[d]
            if 0 < ni < 16 and 0 < nj < 16 and arr[ni][nj] != "1" and visited[ni][nj] == 0:
                stack.append((ni, nj))
                visited[ni][nj] = 1
    
    print(f"#{tc} {1 if visited[ei][ej] else 0}")
        
        
