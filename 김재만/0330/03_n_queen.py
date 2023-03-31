def promising(x, y):
    # 좌상, 상, 우상
    dx = [-1, -1, -1]
    dy = [-1, 0, 1]

    for d in range(3):
        nx = x + dx[d]
        ny = y + dy[d]
        while 0 <= nx < N and 0 <= ny < N:
            if board[nx][ny]:
                return 0
            nx += dx[d]
            ny += dy[d]

    return 1


def f(i, N):
    global cnt

    if i == N:
        cnt += 1
    else:
        for j in range(N):
            if promising(i, j):
                board[i][j] = 1
                f(i + 1, N)
                board[i][j] = 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    board = [[0] * N for _ in range(N)]
    cnt = 0
    f(0, N)
    print(cnt)
