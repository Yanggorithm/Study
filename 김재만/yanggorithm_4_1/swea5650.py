# 핀볼 게임

def pinball(x, y, p_map, k):
    '''
    :param sx: 시작 x 위치
    :param sy: 시작 y 위치
    :param p_map: 핀볼게임 맵
    :param k: 이동 방향
    :return: 점수
    '''
    '''
    k 
    0: 상
    1: 하
    2: 좌
    3: 우
    '''
    score = 0
    # 시작 위치 저장
    sx = x
    sy = y

    while True:

        nx = x + dx[k]
        ny = y + dy[k]

        # 벽을 만난 경우
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            # 반대 방향 전환
            if k % 2 == 0:
                k += 1
            else:
                k -= 1
            score += 1
        # 벽을 안 만났다 => 범위 내에 있다.
        else:
            # 1번 삼각형을 만났다
            if p_map[nx][ny] == 1:
                score += 1
                if k == 0:
                    k = 1
                elif k == 1:
                    k = 3
                elif k == 2:
                    k = 0
                elif k == 3:
                    k = 2
            # 2번 삼각형을 만났다.
            elif p_map[nx][ny] == 2:
                score += 1
                if k == 0:
                    k = 3
                elif k == 1:
                    k = 0
                elif k == 2:
                    k = 1
                elif k == 3:
                    k = 2
            # 3번 삼각형을 만났다.
            elif p_map[nx][ny] == 3:
                score += 1
                if k == 0:
                    k = 2
                elif k == 1:
                    k = 0
                elif k == 2:
                    k = 3
                elif k == 3:
                    k = 1
            # 4번 삼각형을 만났다.
            elif p_map[nx][ny] == 4:
                score += 1
                if k == 0:
                    k = 1
                elif k == 1:
                    k = 2
                elif k == 2:
                    k = 3
                elif k == 3:
                    k = 0
            # 5번 블록을 만났다.
            elif p_map[nx][ny] == 5:
                score += 1
                # 반대 방향 전환
                if k % 2 == 0:
                    k += 1
                else:
                    k -= 1
            # 웜홀을 만났다.
            elif 6 <= p_map[nx][ny] <= 10:
                nx, ny = w_hole[p_map[nx][ny]][w_hole[p_map[nx][ny]].index((nx, ny)) - 1]

            elif (nx == sx and ny == sy) or ((nx, ny) in b_hole):
                return score

        x = nx
        y = ny


T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    p_map = [list(map(int, input().split())) for _ in range(n)]
    w_hole = [[] for _ in range(15)]
    b_hole = []
    max_score = -1

    # 상하좌우
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    for i in range(n):
        for j in range(n):
            for k in range(6, 11):
                if p_map[i][j] == k:
                    # w_hole 리스트의 k번 인덱스에 웜홀 (x,y) 좌표 저장
                    w_hole[k].append((i,j))
                elif p_map[i][j] == -1:
                    b_hole.append((i,j))

    for i in range(n):
        for j in range(n):
            if p_map[i][j] == 0:
                for k in range(4):
                    score = pinball(i, j, p_map, k)
                    if score > max_score:
                        max_score = score

    print(f"#{tc} {max_score}")
