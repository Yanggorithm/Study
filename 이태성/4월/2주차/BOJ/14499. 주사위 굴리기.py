import sys
input = sys.stdin.readline

def is_valid(nr, nc):
    return 0 <= nr < N and 0 <= nc < M

# 1번 인덱스가 위
row_dice = [0, 0, 0, 0]
column_dice = [0, 0, 0, 0]

dr = [0, 0, 0, -1, 1]
dc = [0, 1, -1, 0, 0]

def dice_changer(command):
    # 동쪽
    if command == 1:
        row_dice[0], row_dice[1], row_dice[2], row_dice[3] = row_dice[3], row_dice[0], row_dice[1], row_dice[2]
        column_dice[1] = row_dice[1]
        column_dice[3] = row_dice[3]
    elif command == 2:
        row_dice[0], row_dice[1], row_dice[2], row_dice[3] = row_dice[1], row_dice[2], row_dice[3], row_dice[0]
        column_dice[1] = row_dice[1]
        column_dice[3] = row_dice[3]
    elif command == 3:
        column_dice[0], column_dice[1], column_dice[2], column_dice[3] = column_dice[1], column_dice[2], column_dice[3], column_dice[0]
        row_dice[1] = column_dice[1]
        row_dice[3] = column_dice[3]
    else:
        column_dice[0], column_dice[1], column_dice[2], column_dice[3] = column_dice[3], column_dice[0], column_dice[1], column_dice[2]
        row_dice[1] = column_dice[1]
        row_dice[3] = column_dice[3]

# 세로, 가로, 위치, 명령
N, M, r, c, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))
sr, sc = r, c
for command in commands:
    nr = sr + dr[command]
    nc = sc + dc[command]
    if not is_valid(nr, nc):
        continue
    # 범위가 유효하다는 말이니까
    dice_changer(command)
    if board[nr][nc]:
        row_dice[3] = column_dice[3] = board[nr][nc]
        board[nr][nc] = 0
    else:
        board[nr][nc] = row_dice[3]
    sr, sc = nr, nc
    print(row_dice[1])