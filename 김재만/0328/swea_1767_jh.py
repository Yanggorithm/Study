def dfs(k, cnt, core):
    # k - 코어 번호, cnt - 전선 길이, core - 코어 개수

    global max_core, min_cnt
    if max_core > core + (M - k):  # 앞으로 나오는 모든 코어를 다 선택해도 max_core보다 작으면
        return  # 리턴

    if k == M:  # 코어를 모두 골랐으면 코어개수, 선 길이 확인
        if max_core < core:  # 코어 개수가 더 많으면 무조건 코어가 많은 쪽 선택
            max_core = core
            min_cnt = cnt
        elif max_core == core:  # 코어 개수가 같으면 선 길이가 적은 쪽 선택
            min_cnt = min(min_cnt, cnt)

    else:
        # 상하좌우 선 이을 수 있는지 체크
        r, c = lst[k]  # 코어 선택
        for d in range(4):  # 해당 코어 4가지 방향 전선 이어보기
            cr, cc = r, c
            flag = True  # 코어가 선이랑 연결됐는지 확인하기 위한 flag
            nr = r + dr[d]
            nc = c + dc[d]
            while 0 <= nr < N and 0 <= nc < N:
                # 해당 방향 이동중에 코어가 있거나 전선이 있으면 연결 불가능하므로 flag = False
                if arr[nr][nc] != 0 or v[nr][nc] != 0:
                    flag = False
                    break
                else:
                    cr, cc = nr, nc
                    nr = cr + dr[d]
                    nc = cc + dc[d]

            if flag:  # 해당 방향 이동중에 코어나 전선이 없었다면 이동했던 칸들 모두 방문처리
                # 방문 처리
                nr = r + dr[d]
                nc = c + dc[d]
                while 0 <= nr < N and 0 <= nc < N:
                    v[nr][nc] = 1
                    cnt += 1  # 방문 처리 해줄 때 연결하기까지 필요한 전선의 길이 더해주기
                    cr, cc = nr, nc
                    nr = cr + dr[d]
                    nc = cc + dc[d]
                # 방문 처리 끝

                dfs(k + 1, cnt, core + 1)

                # 방문 해제 처리
                nr = r + dr[d]
                nc = c + dc[d]
                while 0 <= nr < N and 0 <= nc < N:
                    v[nr][nc] = 0
                    cnt -= 1  # 방문 처리 해줄 때 사용했던 전선 길이 다시 빼주기
                    # 해당 칸에 코어가 있거나 전선이 있으면
                    cr, cc = nr, nc
                    nr = cr + dr[d]
                    nc = cc + dc[d]
                # 방문 해제 처리 끝

        # 해당 코어에 아무런 선을 연결하지 않았을 경우에도 체크해주어야 하므로 선 없는 상태에서도 다음 코어 선택하기
        dfs(k + 1, cnt, core)


T = int(input())
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for t in range(1, T + 1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    lst = []
    v = [[0] * N for _ in range(N)]
    M = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                lst.append((i, j))
                M += 1
    max_core = 0
    min_cnt = 144

    dfs(0, 0, 0)
    print(f"#{t}", min_cnt)