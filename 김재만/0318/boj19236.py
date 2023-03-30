# 청소년 상어 (3일에 걸쳐 풀이완료... 너무 힘들어)
import sys
import copy
input = sys.stdin.readline


def dfs(sx, sy, fx, fy, direction, cnt, sea):

    global max_v

    '''
    sx : 상어 움직인 후 위치 x
    sy : 상어 움직인 후 위치 y
    fx : 상어 움직이기 전 위치 x
    fy : 상어 움직이기 전 위치 y
    direction : 상어 방향
    cnt : 먹은 물고기 수
    max_v : 결과값으로 출력할 최대한 먹을 수 있는 양 비교를 위해
    '''

    # 상어가 해당 위치를 잡아먹고 시작
    sea[fx][fy][0] = 0
    sea[fx][fy][1] = 0
    sea[sx][sy][0] = "shark"

    # 물고기가 먼저 움직임
    # 깨끗한바다
    new_sea = copy.deepcopy(sea)
    # 더러운바다
    new_sea = fish_move(sea)

    # 이후 상어가 움직임
    dist = 0
    flag = 3
    
    while True:
        dist += 1
        nx = sx + (dx[direction] * dist)
        ny = sy + (dy[direction] * dist)
        # 상어가 갈 수 있는 곳
        if 0 <= nx < 4 and 0 <= ny < 4 and new_sea[nx][ny][0] != 0:
            re = new_sea[nx][ny][:]
            dfs(nx, ny, sx, sy, new_sea[nx][ny][1], cnt+new_sea[nx][ny][0], new_sea)
            new_sea[nx][ny] = re
            continue
        else:
            max_v = max(max_v, cnt)
            flag -= 1
            if not flag:
                break
            else:
                continue

    return


def fish_xy(sea, fish_num):
    for i in range(4):
        for j in range(4):
            if sea[i][j][0] == fish_num:
                return (i, j, sea[i][j][1])


def fish_move(sea):
    l_sea = copy.deepcopy(sea)
    # 1번부터 시작해서 물고기 번호 찾기 잡아 먹혔을 수도 있음
    for fish_num in range(1, 17):
        fish_position = fish_xy(l_sea, fish_num)
        if fish_position:
            x = fish_position[0]
            y = fish_position[1]
            next_d = fish_position[2]
            while True:
                nx = x + dx[next_d]
                ny = y + dy[next_d]

                # 이동 할 수 있는 위치라면
                if 0 <= nx < 4 and 0 <= ny < 4 and l_sea[nx][ny][0] != 'shark':
                    l_sea[x][y], l_sea[nx][ny] = l_sea[nx][ny], l_sea[x][y]
                    l_sea[nx][ny][1] = next_d
                    break

                next_d = (next_d+1) % 8

    return l_sea


undersea = [[] for _ in range(4)]

for _ in range(4):
    line = list(map(int, input().split()))
    for i in range(0, 8, 2):
        fish = [line[i], line[i+1]-1]
        undersea[_].append(fish)

# 상 좌상 좌 좌하 하 우하 우 우상
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

cnt = 0
start = [0, 0]
max_v = -1

cnt += undersea[0][0][0]
undersea[0][0] = ["shark", undersea[0][0][1]]

dfs(0, 0, 0, 0, undersea[0][0][1], cnt, undersea)
print(max_v)
