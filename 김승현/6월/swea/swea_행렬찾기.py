import sys
sys.stdin = open('행렬찾기.txt', 'r')
from collections import deque

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs로 행렬이 몇 개 있는지 찾으면서
# 행렬의 크기를 알 수 있게함
def bfs(sx, sy, visit, cnt):
    q = deque()
    q.append((sx, sy))
    visit[sx][sy] = cnt

    t_x, t_y = sx, sy

    while q:
        x, y = q.popleft()

        # q에 마지막에 담겨있는 값이 행렬의 마지막 점이므로
        # x, y와 t_x, t_y를 비교해서
        # 갱신을 해준다
        if x >= t_x and y >= t_y:
            t_x = x
            t_y = y

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < n and map_v[nx][ny] != 0 and visit[nx][ny] == 0:
                q.append((nx, ny))
                visit[nx][ny] = cnt


    return t_x, t_y


for test_case in range(1, T + 1):
    n = int(input())

    map_v = [list(map(int, input().split())) for _ in range(n)]

    visited = [[0] * n for _ in range(n)]

    count = 0
    res = []

    for i in range(n):
        for j in range(n):

            if map_v[i][j] != 0 and visited[i][j] == 0:
                count += 1
                # i, j 는 행렬 맨 왼쪽 위 꼭짓점이 되고
                # r_x, r_y는 행렬 맨 오른쪽 아래 꼭짓점이 된다.
                # count변수는 행렬이 몇개 있는지 판단하기 위해 선언
                r_x, r_y = bfs(i, j, visited, count)

                # res리스트는 행렬의 크기를 알 수 있게 함
                # 행, 열, 그리고 행렬의 크기인 (행 * 열)로 구성
                res.append([r_x - i + 1, r_y - j + 1, (r_y - j + 1) * (r_x - i + 1)])

    # 행렬의 크기에 따라서 값을 출력해야하므로 lambda로
    # 행렬의 크기에 따라 정렬을 시킴
    # 행렬의 크기가 같은 경우 행을 기준으로 정렬을 시킴
    res.sort(key = lambda x : (x[2], x[0]))

    # 출력은 먼저 행렬의 갯수이므로
    # 새로운 result 리스트에 넣어줌
    result = [count]

    # 정렬한 res 리스트에 따라서 result에 행, 열을 append시켜줌
    for i in range(count):
        result.append(res[i][0])
        result.append(res[i][1])

    # 출력형식에 맞추어서 결과를 보여줌줌
    print(f'#{test_case}', nd = " ")
    print(*result)