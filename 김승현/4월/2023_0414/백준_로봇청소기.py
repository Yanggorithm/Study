import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]  # 0 북 1 동 2 남 3 서
dy = [0, 1, 0, -1]

# r은 세로 c는 가로
r, c = map(int, input().split())

# x, y 는 시작위치 d는 바라보는 방향
x, y, d = map(int, input().split())

map_list = [list(map(int, input().split())) for _ in range(r)]
visited = [[0] * c for _ in range(r)]
visited[x][y] = 1

# 후진을 할 때 계속 후진하기 위한 flag
flag = 0

# 후진을 할 때 저장하는 변수
pre_d = 0
while True:
    clean = 0
    # 주변 네 곳 중 청소할 곳이 있으면 판단하기 위한 변수
    for t in range(4):
        nx = x + dx[t]
        ny = y + dy[t]

        # 청소하지않은 공간이며, 지나치지 않은곳이면 clean += 1
        if visited[nx][ny] == 0 and map_list[nx][ny] == 0:
            clean += 1

    # 만약 청소할 공간이 있으면
    if clean:
        # flag == 1일때는 후진을 하다가 발견할때
        # 이전 후진하기 전에 방향값을 d에 할당
        if flag == 1:
            d = pre_d
        # 그렇지 않으면
        while True:
            # 청소할 공간이 있을때까지 반시계로 고개를 돌리면서 확인
            d -= 1
            if d < 0:
                d = 3

            temp_x = x + dx[d]
            temp_y = y + dy[d]
            if visited[temp_x][temp_y] == 0 and map_list[temp_x][temp_y] == 0:
                # 확인되면 flag = 0 으로 선언
                flag = 0
                break

    else:
        # flag가 0인경우는 처음 후진하는 경우!
        if flag == 0:
            pre_d = d
            if d == 0:
                d = 2
            elif d == 1:
                d = 3
            elif d == 2:
                d = 0
            else:
                d = 1
            # 처음 후진하는 경우이기에
            # 청소할 공간을 찾지 못하게 된다면
            # 계속 후진해야하기에 flag를 일단 1로 설정!
            flag = 1

    nx = x + dx[d]
    ny = y + dy[d]
    # 만약 다음 공간이 벽이게 되면 break시킨다.
    if map_list[nx][ny] == 1:
        break

    # 벽이 아니면 방문 표시 하고 다음위치로 이동하게
    # x, y를 nx, ny로 할당!
    x, y = nx, ny
    visited[x][y] = 1

# visited배열은 청소를 완료한 공간으로
# visited.count(1)를 통해 숫자를 세서 결과 확인인
result = 0
for i in range(1, r - 1):
    result += visited[i].count(1)

print(result)