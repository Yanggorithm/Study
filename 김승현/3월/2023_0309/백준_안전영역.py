from collections import deque

N = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

map_s = [list(map(int, input().split())) for _ in range(N)]

max_v = 0
for i in range(N):
    if max_v < max(map_s[i]):
        max_v = max(map_s[i])

def dfs(G, map_max):
    result = []
    for k in range(map_max):
        visited = [[0] * N for _ in range(N)]
        cnt = 0
        for i in range(N):
            for j in range(N):
                stack = []
                if not visited[i][j] and G[i][j] > k:
                    x = i
                    y = j
                    visited[x][y] = 1
                    while True:

                        for d in range(4):
                            nx = x + dx[d]
                            ny = y + dy[d]

                            if 0 <= nx < N and 0 <= ny < N and G[nx][ny] > k and not visited[nx][ny]:
                                stack.append((x, y))
                                x = nx
                                y = ny
                                visited[x][y] = 1
                                break

                        else:
                            if stack:
                                x, y = stack.pop()
                            else:
                                cnt += 1
                                break

        result.append(cnt)

    return max(result)

ans = dfs(map_s, max_v)

print(ans)