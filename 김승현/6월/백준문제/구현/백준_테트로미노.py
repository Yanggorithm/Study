import sys
input = sys.stdin.readline

# 위로 갈 필요가 없음
dx = [1, 0, 0]
dy = [0, -1, 1]

# ㅗ 모양 판단하기 위해 새로운 델타배열 사용
garo_x = [1, -1]
garo_y = [0, 0]

sero_x = [0, 0]
sero_y = [1, -1]

N, M = map(int, input().split())
map_v = [list(map(int, input().split())) for _ in range(N)]

max_value = 0


# flag에 따라 가로로 일자인지 세로로일자인지 판단

def check(x, y, block, value, check_gs):
    global max_value

    # block에 4개가 쌓여있다면 확인
    if len(block) == 4:
        max_value = max(max_value, value)
        return

    # 일자의 모양일 때 확인
    if len(block) == 3:
        if check_gs == 1:
            for t in range(2):
                temp_x = block[1][0] + sero_x[t]
                temp_y = block[1][1] + sero_y[t]

                if 0 <= temp_x < N and 0 <= temp_y < M and (temp_x, temp_y) not in block:
                    block.append((temp_x, temp_y))
                    check(temp_x, temp_y, block, value + map_v[temp_x][temp_y], check_gs)
                    block.pop()

        elif check_gs == 2:
            for t in range(2):
                temp_x = block[1][0] + garo_x[t]
                temp_y = block[1][1] + garo_y[t]

                if 0 <= temp_x < N and 0 <= temp_y < M and (temp_x, temp_y) not in block:
                    block.append((temp_x, temp_y))
                    check(temp_x, temp_y, block, value + map_v[temp_x][temp_y], check_gs)
                    block.pop()

    # 블럭들을 조합
    for d in range(3):
        nx = x + dx[d]
        ny = y + dy[d]


        if d == 0 and (check_gs == 4 or check_gs == 1):
            # 세로 일자
            check_gs = 1
        elif (d == 1 or d == 2) and (check_gs == 4 or check_gs == 2):
            # 가로 일자
            check_gs = 2
        else:
            # 그러지 않은 경우
            check_gs = 4

        if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in block:
            block.append((nx, ny))
            check(nx, ny, block, value + map_v[nx][ny], check_gs)
            block.pop()


# 백트래킹을 통해서 확인!
# 가지치기를 하지 않아서 그냥 dfs인가..?

for i in range(N):
    for j in range(M):
        check(i, j, [(i, j)], map_v[i][j], 4)

print(max_value)
