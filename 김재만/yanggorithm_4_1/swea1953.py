# 탈주범 검거

from collections import deque

t_map = {0: (),
         1: ([-1, 0], [1, 0], [0, -1], [0, 1]),  # 상 하 좌 우
         2: ([-1, 0], [1, 0]),  # 상 하
         3: ([0, -1], [0, 1]),  # 좌 우
         4: ([-1, 0], [0, 1]),  # 상 우
         5: ([1, 0], [0, 1]),  # 하 우
         6: ([1, 0], [0, -1]),  # 하 좌
         7: ([-1, 0], [0, -1])}  # 상 좌


def bfs(sx, sy, time):
    q = deque()
    q.append((sx, sy))

    visited = [[False] * m for _ in range(n)]

    # 상하좌우
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    # 처음 맨홀 위치도 체크
    cnt = 1
    visited[sx][sy] = True
    day = 1
    while day < time:
        for _ in range(len(q)):
            x, y = q.popleft()
            # 아래 값에 따라 상하좌우 갈 수 있는 탐색이 달라짐!
            # 1은 상하좌우 4방향 탐색
            # print(t_map[c_map[x][y]])
            for xx, yy in t_map[c_map[x][y]]:
                nx = x + xx
                ny = y + yy

                if 0 <= nx < n and 0 <= ny < m and c_map[nx][ny] != 0 and visited[nx][ny] == False:
                    cc = c_map[nx][ny]
                    # 현재 위치에서 좌로 이동 중이라면 다음 위치 nx,ny 에서 오른쪽으로 뚫려 있어야함
                    if (yy == -1 and cc in [1, 3, 4, 5]) or (yy == 1 and cc in [1, 3, 6, 7]) or (xx == -1 and cc in [1, 2, 5, 6]) or (xx == 1 and cc in [1, 2, 4, 7]):
                        q.append((nx, ny))
                        visited[nx][ny] = True
                        cnt += 1

        day += 1

    return cnt


T = int(input())

for tc in range(1, T + 1):
    n, m, r, c, l = map(int, input().split())

    c_map = [list(map(int, input().split())) for _ in range(n)]

    ans = bfs(r, c, l)
    print(f"#{tc} {ans}")