# 스도쿠
import sys
from collections import deque
input = sys.stdin.readline


def solve_sudoku(sudoku):
    q = deque()

    for i in range(9):
        for j in range(9):
            if not sudoku[i][j]:
                q.append((i, j))
    
    while q:
        x, y = q.popleft()
        possible_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        for i in range(9):
            if sudoku[x][i] in possible_list:
                possible_list.remove(sudoku[x][i])

        for i in range(9):
            if sudoku[i][y] in possible_list:
                possible_list.remove(sudoku[i][y])

        nemo_x = x // 3
        nemo_y = y // 3

        for i in range(nemo_x * 3, nemo_x * 3 + 3):
            for j in range(nemo_y * 3, nemo_y * 3 + 3):
                if sudoku[i][j] in possible_list:
                    possible_list.remove(sudoku[i][j])

        # 추려진 possible_list 를 가지고 돌려보자
        if len(possible_list) == 1:
            sudoku[x][y] = possible_list[0]
        else:
            q.append((x,y))


sudoku = [list(map(int, input().split())) for _ in range(9)]

solve_sudoku(sudoku)
for i in range(9):
    print(" ".join(map(str,sudoku[i])))