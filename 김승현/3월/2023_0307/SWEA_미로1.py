import sys
sys.stdin = open('미로1.txt', 'r')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1 ,1]

def dfs(x, y, n):
    visited = [[0] * n for _ in range(n)]
    stack = []
    res = 0
    visited[x][y] = 1

    while True:
        if num_list[x][y] == '3':
            res = 1
            break

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < n and num_list[nx][ny] != '1' and not visited[nx][ny]:
                stack.append((x, y))
                visited[nx][ny] = 1
                x = nx
                y = ny
                break
        else:
            if stack:
                x, y = stack.pop()
            else:
                break

    return res

for test_case in range(1, 11):
    T = int(input())
    N = 16
    num_list = [list(input()) for _ in range(16)]

    result = dfs(1, 1, N)
    print(f'#{T} {result}')
