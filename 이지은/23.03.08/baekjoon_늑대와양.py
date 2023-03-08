from collections import deque

r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque([])
visited = [[0]*c for _ in range(r)]

def solve():
    global arr

    for i in range(r):
        for j in range(c):
            if arr[i][j] == "W":
                q.append((i, j))
                visited[i][j] = 1
                while q:
                    ci, cj = q.popleft()
                    for d in range(4):
                        ni, nj = ci + dx[d], cj + dy[d]
                        if 0<=ni<r and 0 <= nj < c and visited[ni][nj] == 0:
                            if arr[ni][nj] == ".":
                                q.append((ni, nj))
                                visited[ni][nj] = 1
                            elif arr[ni][nj] == "S":
                                if arr[ci][cj] == "W":
                                    return 0
                                else:
                                    arr[ci][cj] = "D"
    return 1

print(solve())
for i in range(r):
    print("".join(arr[i]))