dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]
tbl = [0, 2, 1, 4, 3]

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    microbe = [list(map(int, input().split())) for _ in range(K)]

    for _ in range(M):
        for i in range(len(microbe)):
            microbe[i][0] = microbe[i][0] + dr[microbe[i][3]]
            microbe[i][1] = microbe[i][1] + dc[microbe[i][3]]
            if microbe[i][0] == 0 or microbe[i][0] == N - 1 or microbe[i][1] == 0 or microbe[i][1] == N - 1:
                microbe[i][2] //= 2
                microbe[i][3] = tbl[microbe[i][3]]

        microbe.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)
        idx = 1
        while idx < len(microbe):
            if microbe[idx-1][0:2] == microbe[idx][0:2]:
                microbe[idx-1][2] += microbe[idx][2]
                microbe.pop(idx)
            else:
                idx += 1

    ans = 0
    for line in microbe:
        ans += line[2]

    print(f"#{tc} {ans}")