## 홈 방범 서비스

from collections import deque

def bfs(sx, sy, k):
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    max_cnt = -1
    # 시작 위치도 저장.
    cnt += city[sx][sy]
    visited[sx][sy] = True
    que = deque()
    que.append((sx,sy))

    # 현재 위치 즉 dist = 1일때 바로 계산
    if dp[k] <= (cnt * m) and max_cnt < cnt:
        max_cnt = cnt

    # print(max_cnt)
    while que:
        for _ in range(len(que)):
            x, y = que.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    cnt += city[nx][ny]
                    que.append((nx,ny))

        k += 1

        if dp[k] <= (cnt * m) and max_cnt < cnt:
            max_cnt = cnt

        if k == n:
            break

    return max_cnt


T = int(input())

dp = [i * i + (i - 1) * (i - 1) for i in range(1, 25)]

for tc in range(1, T + 1):
    n, m = map(int, input().split())

    city = [list(map(int, input().split())) for _ in range(n)]

    ans = -1
    # 상하좌우
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    for i in range(n):
        for j in range(n):
            rlt = bfs(i, j, 0)
            if rlt > ans:
                ans = rlt

    print(f"#{tc} {ans}")
