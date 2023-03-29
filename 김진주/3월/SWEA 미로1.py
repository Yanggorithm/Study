# 시작 좌표(si, sj)/목적지 좌표(ei, ej)
def bfs(si, sj, ei, ej):
    q = []
    q.append((si, sj))
    visit = [[0] * n for _ in range(n)]
    visit[si][sj] = 1

    while q:
        # 현 위치 q 에서 꺼내고 도착 위치랑 같다면 1 반환
        ci, cj = q.pop(0)
        if (ci, cj) == (ei, ej):
            return 1
        # 4 방향 탐색
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            # (ni, nj)가 범위 내에 있고, 방문 기록 없고, 벽('1')이 아니라면
            if 0 <= ni < n and 0 <= nj < n and visit[ni][nj] != 1 and arr[ni][nj] != '1':
                # q에 (ni, nj) 넣고 방문기록(1)
                q.append((ni, nj))
                visit[ni][nj] = 1

    # 도착지점 못갔다면 0 반환
    return 0

t = 10
for tc in range(1, t + 1):
    n = 16
    _ = input()
    arr = [input() for _ in range(n)]
    # print(arr)
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '2':  # 출발지점(2)
                si, sj = i, j
            elif arr[i][j] == '3':  # 도착지점(3)
                ei, ej = i, j

    ans = bfs(si, sj, ei, ej)

    print(f'#{tc} {ans}')