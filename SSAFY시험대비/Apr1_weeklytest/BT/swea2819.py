# 격자판 이어붙이기

def game_start(x, y):
    if len(result) == 7:
        ans.add(tuple(result))
        return

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < 4 and 0 <= ny < 4:
            result.append(t_map[nx][ny])
            game_start(nx, ny)
            result.pop()


T = int(input())

for tc in range(1, T + 1):
    t_map = [list(map(int, input().split())) for _ in range(4)]

    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    result = []
    ans = set()

    for i in range(4):
        for j in range(4):
            result.append(t_map[i][j])
            game_start(i, j)
            result.pop()

    print(f"#{tc} {len(ans)}")
