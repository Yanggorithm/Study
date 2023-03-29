'''
8*8 체스보드
n 개의 퀸을 서로 다른 두 퀸이 공격하지 못하게 놓는 경우의 수
'''

def backtracking(row, remain):
    global cnt

    # 1. 종료 조건
    if row == n and remain == 0:
        cnt += 1
        return

    # 2. 재귀 호출
    # 현재 행 row 에서 i 번째 열에 퀸 놓을 수 있는지
    for i in range(n):
        place = True

        # 세로에 퀸 있는지 검사
        for j in range(row):
            if board[j][i] == 1:
                place = False
                break
        # 대각선에 퀸 있는지 검사
        for j in range(1, row + 1):
            # 좌상
            if row - j >= 0 and i - j >= 0 and board[row - j][i - j] == 1:
                place = False
                break
            # 우상
            if row - j >= 0 and i + j < n and board[row - j][i + j] == 1:
                place = False
                break

        # 퀸 놓을 수 있는지 검사
        if place:
            # 놓을 수 있다면, 현 위치에 놓고 다음 위치로 이동
            board[row][i] = 1
            backtracking(row + 1, remain - 1)
            # 다시 되돌려놓고 진행할 수 있도록 초기화
            board[row][i] = 0

t = int(input())
for tc in range(1, t+1):
    n = int(input())

    cnt = 0

    board = [[0] * n for _ in range(n)]
    print(board)
    backtracking(0, n)

    print(f'#{tc} {cnt}')

'''
2
1
2

1
0
'''