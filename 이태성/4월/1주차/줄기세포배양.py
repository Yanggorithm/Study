dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    now_time = 0
    cell = [set() for _ in range(11)]
    for r in range(N):
        row_line = list(map(int, input().split()))
        for c in range(M):
            tmp = row_line[c]
            if tmp:
                cell[tmp].add((r, c))
    cnt = 1
    while cnt < K:
        for i in range(1, 11):
            if cnt % (i+1) == 0 and cell[i]:
                new_cell = set()
                while cell[i]:
                    r, c = cell[i].pop()
                    for d in range(4):
                        nr = r + dr[d]
                        nc = c + dc[d]
                        new_cell.add((nr, nc))
                cell[i] = new_cell
        cnt += 1
    ans = set()
    for i in range(1, 11):
        ans = ans.union(cell[i])
    print(len(ans))