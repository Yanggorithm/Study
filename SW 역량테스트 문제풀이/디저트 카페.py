def is_valid(nr, nc):
    return 0 <= nr < N and 0 <= nc < N

# 출발 위치, 경로, 회전 횟수, 길이
def dfs(r, c, path, turn, length):
    global maxL, start

    # [1] 종료 조건
    # 3번 0에서부터 3까지 돌아야하고 그게 시작지점이어야만 종료
    if turn == 3 and (r, c) == start:
        maxL = max(maxL, length)
        return

    # [2] 유효성 검증
    # 값이 범위를 벗어나지 않았는지 확인하고,
    # 지금 가는 경로에서 처음 먹는 디저트라면 True
    if is_valid(r, c) and D_cafe[r][c] not in path:
        nr = r + dr[turn]
        nc = c + dc[turn]
        # 우선 지금 한 번 돌고 가능한데
        dfs(nr, nc, path + [D_cafe[r][c]], turn, length + 1)

        # 더 돌 수 있다면
        # [3] 특이 조건
        # 일단 꺾고 보자.
        if turn < 3:
            nr = r + dr[turn + 1]
            nc = c + dc[turn + 1]
            dfs(nr, nc, path + [D_cafe[r][c]], turn + 1, length + 1)

# 움직이는 방향이 정해짐
dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    D_cafe = [list(map(int, input().split())) for _ in range(N)]
    # 4번 돌아야 한다.
    maxL = -1
    for sr in range(N - 1):
        for sc in range(1, N - 1):
            start = (sr, sc)
            dfs(sr, sc, [], 0, 0)

    print(f"#{tc} {maxL}")