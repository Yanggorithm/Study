import sys
input = sys.stdin.readline
from pprint import pprint
# 각각의 칸은 벽 또는 빈칸이다
# 처음빈칸은 청소되지 않은 상태

# 현재칸이 아직 청소되지 않은경우, 현재 칸을 청소

# 현재 칸의 주변 4칸이 다 청소가 된 경우
# 1. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
# 2. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.

# 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
# 1. 반시계 방향으로 90도 회전한다.
# 2. 바라보는 방향을 기준으로

dx = [-1, 0, 1, 0]  # 0 북 1 동 2 남 3 서
dy = [0, 1, 0, -1]

r, c = map(int, input().split())
x, y, d = map(int, input().split())

map_list = [list(map(int, input().split())) for _ in range(r)]
visited = [[0] * c for _ in range(r)]
visited[x][y] = 1

flag = 0
while True:
    clean = 0
    for t in range(4):
        nx = x + dx[t]
        ny = y + dy[t]

        if visited[nx][ny] == 0 and map_list[nx][ny] == 0:
            clean += 1

    if clean:
        for i in range(4):
            d = (i + d) % 4
            temp_x = x + dx[d]
            temp_y = y + dy[d]
            if visited[temp_x][temp_y] == 0 and map_list[temp_x][temp_y] == 0:
                break
            flag = 0

    else:
        if flag == 0:
            if d == 0:
                d = 2
            elif d == 1:
                d = 3
            elif d == 2:
                d = 0
            else:
                d = 1

            flag = 1

    nx = x + dx[d]
    ny = y + dy[d]

    if map_list[nx][ny] == 1:
        break

    x, y = nx, ny
    visited[x][y] = 1

result = 0
for i in range(r):
    result += sum(visited[i])

print(result)
pprint(visited)