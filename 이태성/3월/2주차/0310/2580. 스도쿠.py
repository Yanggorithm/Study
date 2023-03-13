import sys
from collections import deque
input = sys.stdin.readline
sudoku = []
blank = deque()
for i in range(9):
    sudoku.append(list(map(int, input().split())))
    for j in range(9):
        if sudoku[i][j] == 0:
            blank.append((i, j))

def check_row(r, num):
    for c in range(9):
        if num == sudoku[r][c]:
            return False
    return True

def check_col(c, num):
    for r in range(9):
        if num == sudoku[r][c]:
            return False
    return True

def check_nine(r, c, num):
    nr = r // 3 * 3
    nc = c // 3 * 3
    for i in range(3):
        for j in range(3):
            if num == sudoku[nr+i][nc+j]:
                return False
    return True

def dfs(idx):
    if idx == len(blank):
        for line in sudoku:
            print(*line)
        exit(0)

    for num in range(1, 10):
        r = blank[idx][0]
        c = blank[idx][1]
        if check_row(r, num) and check_col(c, num) and check_nine(r, c, num):
            sudoku[r][c] = num
            dfs(idx+1)
            sudoku[r][c] = 0

dfs(0)