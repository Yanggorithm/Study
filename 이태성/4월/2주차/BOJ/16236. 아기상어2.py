import sys
from collections import deque
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def is_valid(nr, nc):
    return 0 <= nr < N and 0 <= nc < N

def bfs():
    global sr, sc, eat, fish, time

    q = deque([(sr, sc)])
    V = [[0 for _ in range(N)] for _ in range(N)]
    V[sr][sc] = 1
    # 최단 거리에 있는 먹을 수 있는 물고기
    shortD = 9999
    can_eat_fish = []
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            # 값이 유효하고 아기상어의 크기보다 작거나 같고 방문하지 않았다면
            if is_valid(nr, nc) and sea[nr][nc] <= size and V[nr][nc] == 0:
                # 거리를 방문배열에 저장해주고
                V[nr][nc] = V[r][c] + 1
                # q에 저장
                q.append((nr, nc))

                # 갈 곳에 물고기가 있다면
                if sea[nr][nc]:
                    # 방문할 곳이 지금 먹을 예정인 물고기의 거리보다 멀다면 q를 비우고 break
                    if V[nr][nc] > shortD:
                        q = []
                        break

                    # size 보다 작고 거리가 작거나 같을 경우
                    if sea[nr][nc] < size:
                        shortD = V[nr][nc]
                        can_eat_fish.append((nr, nc))

    # print(sr, sc)
    # print(can_eat_fish, time, eat, size)
    if can_eat_fish:
        # 가장 위 고르고 가장 왼쪽 고르고
        can_eat_fish.sort(key=lambda x:(x[0], x[1]))
        xr, xc = can_eat_fish[0]
        # 물고기 먹고 0으로 시체 처리
        sea[xr][xc] = 0

        # 먹었으니까 1 추가
        eat += 1

        # 시간에다가 지금까지의 거리에서 1빼준다.
        time += shortD - 1

        # 먹은 자리에 상어의 위치를 바꿔준다.
        sr, sc = xr, xc
    else:
        # 물고기를 하나도 못 먹을 경우
        fish = False


N = int(input())
sea = []
sr = sc = 0
for r in range(N):
    sea.append(list(map(int, input().split())))
    for c in range(N):
        if sea[r][c] == 9:
            sr, sc = r, c

fish = True
sea[sr][sc] = 0
size, eat, time = 2, 0, 0

# 먹을 수 있는 물고기가 있을 때만 실행되는 반복문
while fish:
    bfs()
    # 크기 만큼 먹었을 때 먹은 양을 초기화 하고 크기 키워주기
    if eat == size:
        eat = 0
        size += 1

print(time)