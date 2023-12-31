import sys
# 물고기가 이동하기 전과 이동한 후를 비교해야 하기 때문에
# copy를 이용해서 deep copy를 해줄 예정
# 이렇게 해야 원본 2차원 배열을 수정하지 않을 수 있다.
# 즉 물고기가 이동하기 전에 움직이고
# 움직이고 나서는 copy를 이용해서 리턴해줄 예정
import copy
input = sys.stdin.readline
# 8방향 탐색 델타배열
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]

# 공간을 벗어나지 않게 하는 함수
def is_valid(nr, nc):
    return 0 <= nr < 4 and 0 <= nc < 4

# 물고기 이동
def move_fish(under_the_sea, sr, sc):
    # 물고기 순차적 이동
    # 물고기의 번호를 먼저 찾아보고 생사여부를 확인하고 살아있으면 바꿔준다.
    # 죽은 물고기는 이동하지 않기 때문에 이렇게 해야한다.
    for no in range(1, 17):
        f_r = f_c = -1
        for r in range(4):
            for c in range(4):
                # 0번째에 생사 여부를 넣었기 때문에 확인해준다.
                # 살아 있는지 먼저 확인하고 번호를 확인하면 연산 횟수를 줄일 수 있을 것이다.
                f_no = under_the_sea[r][c][0]
                if f_no == no:
                    f_r, f_c = r, c
                    break
        if f_r == f_c == -1:
            continue
        f_dir = under_the_sea[f_r][f_c][1]

        for d in range(8):
            nd = (d + f_dir) % 8
            nr = f_r + dr[nd]
            nc = f_c + dc[nd]
            # 공간이 유효하고
            # 빈칸이어도 가고
            # 상어만 아니면 된다.
            # 이 부분이 잘못됨.
            # 상어를 피해주지 않아서 생긴 문제
            if is_valid(nr, nc) and (nr, nc) != (sr, sc):
                under_the_sea[f_r][f_c][1] = nd
                fish_swap(under_the_sea, f_r, f_c, nr, nc)
                break
# cuts 는 copy_under_the_sea를 줄임
def fish_swap(uts, f_r, f_c, nr, nc):
    uts[nr][nc], uts[f_r][f_c] = uts[f_r][f_c], uts[nr][nc]

# 상어 이동
# 이게 dfs형태로 간다.
def shark_move(under_the_sea, sr, sc, eat):
    global max_eat
    eat += under_the_sea[sr][sc][0]
    max_eat = max(max_eat, eat)
    # 일단 물고기 잡아먹고
    under_the_sea[sr][sc][0] = 0

    # 물고기 움직이기
    move_fish(under_the_sea, sr, sc)

    # dfs 시작
    # 상어가 한 방향으로 얼마나 갈지 정해주기
    srd = under_the_sea[sr][sc][1]
    for i in range(1, 4):
        nsr = sr + dr[srd]*i
        nsc = sc + dc[srd]*i
        if is_valid(nsr, nsc) and under_the_sea[nsr][nsc][0]:
            copy_under_the_sea = copy.deepcopy(under_the_sea)
            # for line in copy_under_the_sea:
            #     print(line)
            # print(sr, sc, "=================")
            shark_move(copy_under_the_sea, nsr, nsc, eat)

# input
# 바다속의 물고기를 3차원 배열로 저장해준다.
under_the_sea = []
for _ in range(4):
    line = list(map(int, input().split()))
    new_line = []
    for i in range(4):
        # 상어가 잡아먹으면 0으로 바꿈
        # 물고기의 번호와 방향
        fish_no = line[i*2]
        # 1을 빼주는 이유 : 1번 부터 8번을 0~7로 바꿔줘야 하기 때문에
        fish_dir = line[i*2+1] - 1
        new_line.append([fish_no, fish_dir])
    under_the_sea.append(new_line)

# 변수 설정
# 상어가 먹은 물고기 최대 합
max_eat = 0
shark_move(under_the_sea, 0, 0, 0)
print(max_eat)