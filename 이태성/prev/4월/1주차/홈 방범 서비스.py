from collections import deque

def is_valid(nr, nc):
    return 0 <= nr < N and 0 <= nc < N

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(sr, sc):
    q = deque()
    q.append((sr, sc))
    V = [[0 for _ in range(N)] for _ in range(N)]
    V[sr][sc] = 1
    cnt_home = 1
    prev = 0
    ans = 0
    while q:
        r, c = q.popleft()

        # 범위 V[r][c]
        # 찾은 집의 수
        if prev != V[r][c]:
            now_cnt = cnt_home
            if s_map[r][c] == 1:
                now_cnt = cnt_home - 1

            price = prev ** 2 + (prev - 1) ** 2
            if prev > 0:
                if (now_cnt*M - price) >= 0:
                    ans = now_cnt
                else:
                    return ans
            prev = V[r][c]

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if is_valid(nr, nc) and V[nr][nc] == 0:
                V[nr][nc] = V[r][c] + 1
                if s_map[nr][nc] == 1:
                    cnt_home += 1
                q.append((nr, nc))

def maxK(dp):
    ans = -1
    for k in range(1, N):
        if dp[k][0] >= 0:
            ans = dp[k][1]
    return ans

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 집의 위치를 넣어줄 리스트
    # 집이 없는 곳부터 찾을 필요는 없기 때문에 만들어준다.
    home = []
    s_map = []
    for r in range(N):
        row_line = list(map(int, input().split()))
        for c in range(N):
            if row_line[c] == 1:
                home.append((r, c))
        s_map.append(row_line)

    max_Home = 0
    for sr, sc in home:
        max_Home = max(bfs(sr, sc), max_Home)

    print(f"#{tc} {max_Home}")
