import sys
input = sys.stdin.readline

# 이다솜파 => S 임도연파 => Y
# 이다솜파가 적어도 7명중에 4명이상 있어야함

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


map_v = [list(input().strip()) for _ in range(5)]


# 소문난 칠공주 결성 경우의 수
result = 0



def check(x, y, visit, scnt, ycnt):
    global result
    if ycnt >= 4:
        return

    if ycnt + scnt == 7:
        for i in range(5):
            print(visit[i])
        print('-------------')
        result += 1
        return



    for d in range(4):

        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < 5 and 0 <= ny < 5 and not visit[nx][ny]:
            if map_v[nx][ny] == 'Y':
                ycnt += 1
                visit[nx][ny] = 1
                check(nx, ny, visit, scnt, ycnt)
                visit[nx][ny] = 0
                ycnt -= 1

            elif map_v[nx][ny] == 'S':
                scnt += 1
                visit[nx][ny] = 1
                check(nx, ny, visit, scnt, ycnt)
                visit[nx][ny] = 0
                scnt -= 1


count = 0
for i in range(5):
    for j in range(5):
        visited = [[0] * 5 for _ in range(5)]
        y_cnt = 0
        s_cnt = 0
        check(i, j, visited, y_cnt, s_cnt)

print(result // 2)