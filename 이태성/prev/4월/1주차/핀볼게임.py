from collections import deque

def is_valid(nr, nc):
    return 0 <= nr < N and 0 <= nc < N

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

block = [
    [],
    [1, 3, 0, 2],
    [3, 0, 1, 2],
    [2, 0, 3, 1],
    [1, 2, 3, 0],
    [1, 0, 3, 2]
]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    game, start, worm_hole = [], [], [[] for _ in range(5)]
    for r in range(N):
        game.append(list(map(int, input().split())))
        for c in range(N):
            tmp = game[r][c]
            if tmp == 0:
                start.append((r, c))
            elif 6 <= tmp <= 10:
                worm_hole[tmp-6].append((r, c))

    max_point = 0
    for sr, sc in start:
        for d in range(4):
            point = 0
            q = deque()
            q.append((sr, sc))
            nd = d
            while q:
                r, c = q.popleft()
                nr, nc = r + dr[nd], c + dc[nd]
                if (nr, nc) == (sr, sc):
                    break

                if is_valid(nr, nc):
                    if game[nr][nc] == 0:
                        q.append((nr, nc))
                    elif game[nr][nc] == -1:
                        # 끝나야지
                        break
                    # 웜홀을 만났을 때
                    elif 6 <= game[nr][nc] <= 10:
                        for nnr, nnc in worm_hole[game[nr][nc]-6]:
                            if (nr, nc) != (nnr, nnc):
                                q.append((nnr, nnc))
                    else:
                        # 포인트 적립
                        point += 1
                        q.append((nr, nc))
                        # 방향 설정
                        nd = block[game[nr][nc]][nd]

                else:
                    point = point * 2 + 1
                    break

            # 연산이 끝나고 나왔을 때
            max_point = max(max_point, point)
    print(f"#{tc} {max_point}")