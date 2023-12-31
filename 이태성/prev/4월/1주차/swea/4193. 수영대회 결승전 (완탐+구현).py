from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def is_valid(nr, nc):
    return 0 <= nr < N and 0 <= nc < N

def bfs(sr, sc, ar, ac):
    q = deque()
    q.append((sr, sc))
    V[sr][sc] = 0
    while q:
        r, c = q.popleft()
        if (r, c) == (ar, ac):
            return True
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if is_valid(nr, nc):
                # 섬인경우 지나가유
                if pool[nr][nc] == 1:
                    continue
                # 소용돌이 인 경우
                tmp = 1
                if pool[nr][nc] == 2:
                    if (V[r][c] + 1) % 3 == 1:
                        tmp += 2
                    elif (V[r][c] + 1) % 3 == 2:
                        tmp += 1

                if V[nr][nc] > V[r][c] + tmp:
                    V[nr][nc] = V[r][c] + tmp
                    q.append((nr, nc))

    return False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 소용돌이 2, 섬 1
    V = [[10**6 for _ in range(N)] for _ in range(N)]
    pool = [list(map(int, input().split())) for _ in range(N)]
    sr, sc = map(int, input().split())
    ar, ac = map(int, input().split())
    ans = -1
    if bfs(sr, sc, ar, ac):
        ans = V[ar][ac]
    print(f"#{tc} {ans}")