T = int(input())
# 설치 해야 하는지 확인
# 설치할 수 있는지 확인
# 이미 설치 되어있는지 확인

for tc in range(1, T+1):
    N, X = map(int, input().split())
    test_map = [list(map(int, input().split())) for _ in range(N)]

    row_visited = [[0 for _ in range(N)] for _ in range(N)]
    column_visited = [[0 for _ in range(N)] for _ in range(N)]
    possible_cnt = 0
    for r in range(N):
        # 왼쪽 부터 확인
        # 왼쪽 바로 직전 높이
        prev_left = test_map[r][0]
        # 길이를 측정할 dp_left
        dp_left = [1 for _ in range(N)]
        # 현재 행은 우선 가능하다고 판단
        this_row_possible = True
        # 왼쪽 1번 인덱스부터 확인
        for c in range(1, N):
            # 현재 높이
            now_height = test_map[r][c]
            # 현재 높이가 전 높이랑 같으면 길이 측정
            if now_height == prev_left:
                # 전에 있는 길이랑 현재 길이를 더해
                dp_left[c] = dp_left[c-1] + 1
            # 현재 높이가 직전 높이보다 1만큼 큰 경우
            elif now_height - 1 == prev_left:
                # 직전 dp_left에 평평한 길이가 X보다 크거나 같은지 확인
                if dp_left[c-1] >= X:
                    # 경사로를 만들 수 있으므로 반복문 실행
                    for q in range(c-1, c-1-X, -1):
                        row_visited[r][q] = 1
                # 경사로를 만들지 못하므로 False 이면서 반복문 종료
                else:
                    this_row_possible = False
                    break
            # 직전 높이가 1이 크더라도 여기서는 거르면 안되므로 pass
            elif now_height + 1 == prev_left:
                pass
            # 그 밖에는 높이가 2 이상 차이나므로 False
            else:
                this_row_possible = False
                break
            prev_left = test_map[r][c]

        # 오른쪽 부터 확인
        # 우선 가능한 행만 확인을 위해 조건문 실행
        if this_row_possible:
            prev_right = test_map[r][-1]
            dp_right = [1 for _ in range(N)]
            # 왼쪽 -2번 인덱스부터 확인
            for c in range(N-2, -1, -1):
                now_height = test_map[r][c]
                if now_height == prev_right:
                    dp_right[c] = dp_right[c+1] + 1
                elif now_height - 1 == prev_right:
                    if dp_right[c+1] >= X:
                        for q in range(c+1, c+1+X):
                            if row_visited[r][q]:
                                this_row_possible = False
                                break
                        if not this_row_possible:
                            break
                    else:
                        this_row_possible = False
                        break
                elif now_height + 1 == prev_right:
                    pass
                else:
                    this_row_possible = False
                    break
                prev_right = test_map[r][c]
        possible_cnt += this_row_possible

    for c in range(N):
        this_column_possible = True
        prev_down = test_map[0][c]
        dp_down = [1 for _ in range(N)]
        for r in range(1, N):
            now_height = test_map[r][c]
            if now_height == prev_down:
                dp_down[r] = dp_down[r-1] + 1
            elif now_height - 1 == prev_down:
                if dp_down[r-1] >= X:
                    for p in range(r-1, r-1-X, -1):
                        column_visited[p][c] = 1
                else:
                    this_column_possible = False
                    break
            elif now_height + 1 == prev_down:
                pass
            else:
                this_column_possible = False
                break
            prev_down = test_map[r][c]
        if this_column_possible:
            prev_up = test_map[-1][c]
            dp_up = [1 for _ in range(N)]
            # 왼쪽 -2번 인덱스부터 확인
            for r in range(N-2, -1, -1):
                now_height = test_map[r][c]
                if now_height == prev_up:
                    dp_up[r] = dp_up[r + 1] + 1
                elif now_height - 1 == prev_up:
                    if dp_up[r+1] >= X:
                        for p in range(r+1, r+1+X):
                            if column_visited[p][c]:
                                this_column_possible = False
                                break
                        if not this_column_possible:
                            break
                    else:
                        this_column_possible = False
                        break
                elif now_height + 1 == prev_up:
                    pass
                else:
                    this_column_possible = False
                    break
                prev_up = test_map[r][c]
        possible_cnt += this_column_possible
    print(f"#{tc}", possible_cnt)