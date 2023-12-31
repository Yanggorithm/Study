from collections import deque
import copy

def is_valid(nr, nc):
    return 0 <= nr < H and 0 <= nc < W

# 정점의 위치를 저장해주는 함수
def find_V(game):
    stack = []
    # 열단위로 찾아야한다.
    for c in range(W):
        for r in range(H):
            if game[r][c]:
                stack.append((r, c))
                break
    return stack

# 다시 쌓는 함수
def compression(game):
    for c in range(W):
        # 거꾸로 탐색하면서 채워주기
        for r in range(H-1, -1, -1):
            if game[r][c]:
                for xr in range(H-1, r, -1):
                    if game[xr][c] == 0:
                        game[xr][c], game[r][c] = game[r][c], game[xr][c]
                        break
    return

# 다시 쌓는 함수2
def new_compression(game):
    for c in range(W):
        idx = H - 1
        for r in range(H-1, -1, -1):
            if game[r][c]:
                game[idx][c], game[r][c] = game[r][c], game[idx][c]
                idx -= 1
    return

# 남은 블럭의 개수를 새주는 함수
def counting(game):
    cnt = 0
    for r in range(H):
        for c in range(W):
           if game[r][c]:
               cnt += 1
    return cnt

# 폭발 함수
def bomb(game, sr, sc):
    q = deque()
    q.append((sr, sc))
    while q:
        r, c = q.popleft()
        tmp = game[r][c] - 1
        game[r][c] = 0
        # 좌우 0으로 만들고
        # 만들면서 1 보다 큰 수를 q에 넣는다.
        for nc in range(max(c-tmp, 0), min(c+tmp+1, W)):
            if game[r][nc] > 1:
                q.append((r, nc))
            else:
                game[r][nc] = 0
        # 상하 0으로 만들기
        for nr in range(max(r-tmp, 0), min(r+tmp+1, H)):
            if game[nr][c] > 1:
                q.append((nr, c))
            else:
                game[nr][c] = 0

# 백트래킹 함수
def dfs(game, now_cnt):
    now_block = counting(game)
    if now_cnt == N or now_block == 0:
        global min_block
        min_block = min(min_block, now_block)
        return
    for sr, sc in find_V(game):
        # deepcopy 보다 line.copy가 더 빠르다.
        # new_game = copy.deepcopy(game)
        new_game = [line.copy() for line in game]
        bomb(new_game, sr, sc)
        new_compression(new_game)
        dfs(new_game, now_cnt+1)

T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    game = [list(map(int, input().split())) for _ in range(H)]
    min_block = 10**9
    dfs(game, 0)
    print(f"#{tc} {min_block}")