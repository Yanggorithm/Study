dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    cultivate = [[0]*(M+K*2) for _ in range(N+K*2)]
    stem_cells = []
    for r in range(N):
        row = list(map(int, input().split()))
        for c in range(M):
            cnt_cells = row[c]
            if cnt_cells > 0:
                cultivate[K+r][K+c] = [cnt_cells, cnt_cells]
                stem_cells.append([K+r, K+c])

    for time in range(K):
        new_cells = []
        for r, c in stem_cells:
            if cultivate[r][c][1] > 0:
                cultivate[r][c][1] -= 1
            elif cultivate[r][c][1] == 0:
                tmp = cultivate[r][c][0]
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if cultivate[nr][nc] == 0:
                        new_cells.append([nr, nc, tmp])
                cultivate[r][c][1] -= 1
                cultivate[r][c][0] -= 1
            else:
                if cultivate[r][c][0] > 0:
                    cultivate[r][c][0] -= 1

        for nc in new_cells:
            r, c, tmp = nc
            if cultivate[r][c] == 0:
                cultivate[r][c] = [tmp, tmp]
                stem_cells.append([r, c])
            else:
                if cultivate[r][c][0] < tmp:
                    cultivate[r][c] = [tmp, tmp]
    ans = 0
    for r in range(N+K*2):
        for c in range(M+K*2):
            if cultivate[r][c] and cultivate[r][c][0] > 0:
                ans += 1

    print(f"#{tc} {ans}")