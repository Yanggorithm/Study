dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    land = []
    cnt = 0
    stack = []
    for i in range(h):
        for j in range(w):
            if arr[i][j]:
                land.append((i, j))
    
    for li, lj in land:
        if arr[li][lj] and visited[li][lj] == 0:
            visited[li][lj] = 1
            cnt += 1
            stack = [(li, lj)]

            while stack:
                ci, cj = stack.pop()
                for d in range(8):
                    ni, nj = ci + dx[d], cj + dy[d]
                    if 0 <= ni < h and 0 <= nj < w and visited[ni][nj] == 0 and arr[ni][nj]:
                        visited[ni][nj] = 1
                        stack.append((ni, nj))
    
    print(cnt)
