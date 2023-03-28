# python 시간초과, pypy 통과

# 빈칸이 어디 있는지 찾는다
# 빈칸에 1~9까지 넣어보고, 행, 열, 박스를 확인한다.
# 해당 자리에 들어갈 수 있으면 숫자를 넣고 넘어간다.
import sys
# 입력
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(9)]

# 빈칸 찾기
blank = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            blank.append((i, j))

def row_check(a, i):
    if a in arr[i]:
        return False
    return True

def column_check(a, j):
    for i in range(9):
        if arr[i][j] == a:
            return False
    return True

def box_check(a, i, j):
    ti, tj = i//3*3, j//3*3
    for bi in range(ti, ti+3):
        for bj in range(tj, tj+3):
            if arr[bi][bj] == a:
                return False
    return True

stop = False
def solve(x):
    global arr, stop
    if x == len(blank):
        stop = True
        print()
        for i in arr:
            print(' '.join(map(str, i)))
        return
    
    row = blank[x][0]
    col = blank[x][1]
    for num in range(1,10):
        if row_check(num, row) and column_check(num, col) and box_check(num, row, col):
            arr[row][col] = num
            solve(x+1)
            arr[row][col] = 0
            if stop:
                return

solve(0)
