# NxN 크기의 공간, 물고기 M마리 아기 상어 1마리
# 초기 아기상어의 크리 2
# 자신의 크기보다 작은 물고기만 먹을 수 있음
# 크기가 같은 물고기는 먹을 수 있찌만, 그 칸은 지날 수 있음

# 더 이상 먹을 수 있는 물고기가 공간에 없다면 엄마 상어에게 도움
# 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러감
# 먹을 수 잇는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러감
# -> 거리가 가까운 물고기가 많다면 가장 왼쪽에 있는 물고기를 먹는다.

import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input())

# 아기 상어 초기 위치
sx, sy = 0, 0

# 잡아먹을 수 있는 시간
time = 0

# 상어의 크기
shark = 2

# map_v을 받으면서 아기 상어 초기 위치 찾기
map_v = []
for j in range(N):
    t = list(map(int, input().split()))
    if 9 in t:
        sx = j
        for i in range(N):
            sy += 1
            if t[i] == 9:
                sy = i
                break

    map_v.append(t)


def bfs(s_x, s_y):
    global shark

    q = deque()
    visited = [[0] * N for _ in range(N)]
    distance = [[0] * N for _ in range(N)]
    visited[s_x][s_y] = 1
    q.append((s_x, s_y))

    # 잡아먹은 개체 카운트
    eating = []

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:

                # 물고기가 상어보다 크기가 작으면
                if map_v[nx][ny] <= shark:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    # 이동했다는 표시로 거리 +1
                    distance[nx][ny] = distance[x][y] + 1
                    if 0 < map_v[nx][ny] < shark:
                        # 만약 물고기가 상어보다 크기가 작다면
                        # 먹을 리스트에 넣어줌
                        eating.append((nx, ny, distance[nx][ny]))

    # 거리순 위에 있는기준 제일 왼쪽에 있는 기준을 나타내기 위해
    # sorted함수로 정리
    return sorted(eating, key=lambda x: (-x[2], -x[0], -x[1]))


# 잡아먹은 개체수
cnt = 0

while True:
    # 시작
    eat_fish = bfs(sx, sy)

    # 먹을 물고기가 없음
    if len(eat_fish) == 0:
        break

    # 제일 조건에 맞는 물고기를 먹은 좌표를 표시
    n_x, n_y, dist = eat_fish.pop()

    # 먹었으니 거리 값이 즉 시간으로 시간에 플러스
    time += dist
    # 먹었다는 의미로 처음 좌표와 먹을 물고기 좌표를 초기화
    map_v[sx][sy], map_v[n_x][n_y] = 0, 0

    # 처음 아기 상어 좌표를 먹은 좌표로 움직여주고
    sx, sy = n_x, n_y

    # 물고기 섭취 +1
    cnt += 1

    # 물고리를 자신의 크기만큼 먹었다면
    # 상어몸집을 키워주고 cnt값을 초기화
    if cnt == shark:
        shark += 1
        cnt = 0

print(time)
