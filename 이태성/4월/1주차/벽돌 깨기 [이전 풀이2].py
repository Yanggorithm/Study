from collections import deque
import copy

def is_valid(nr, nc):
    return 0 <= nr < H and 0 <= nc < W

def bfs(sr, sc, new_game):
    q = deque([(sr, sc)])
    while q:
        r, c = q.popleft()
        for k in range(1, new_game[r][c]):
            for d in range(4):
                nr = r + dr[d] * k
                nc = c + dc[d] * k
                if is_valid(nr, nc) and new_game[nr][nc]:
                    if new_game[nr][nc] > 1:
                        q.append((nr, nc))
                    else:
                        new_game[nr][nc] = 0
        new_game[r][c] = 0
    # 여기서 재 배치까지
    for c in range(W):
        idx = H - 1
        for r in range(H - 1, -1, -1):
            if new_game[r][c]:
                new_game[idx][c], new_game[r][c] = new_game[r][c], new_game[idx][c]
                idx -= 1

# 백트래킹
def backtracking(S, now_game):
    global min_counting
    now_counting = counting(now_game)
    if S == N or now_counting == 0:
        if min_counting > now_counting:
            min_counting = now_counting
        return
    else:
        result = finder(now_game)
        for r, c in result:
            new_game = copy.deepcopy(now_game)
            bfs(r, c, new_game)
            backtracking(S + 1, new_game)

# 맨 위에 행만 찾아주는 함수
def finder(new_game):
    result = []
    for i in range(W):
        for j in range(H):
            if new_game[j][i] >= 1:
                result.append((j, i))
                break
    return result

# 남아있는 블록의 수를 새는 함수
def counting(new_game):
    cnt = 0
    for i in range(H):
        for j in range(W):
            if new_game[i][j] > 0:
                cnt += 1
    return cnt

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    game = [list(map(int, input().split())) for _ in range(H)]
    # W 중에서 어디에 떨어 트릴지 결정해야 한다.
    # 0에만 떨어트렸을 때
    # 1에만 떨어트렸을 때
    # 2에만 떨어트렸을 때
    # 연쇄 작용이 많이 일어나는 지점을 찾는다.
    # (연쇄작용 폭발 값, R, C)
    min_counting = 15 * 12
    backtracking(0, game)
    print(f"#{tc}", min_counting)