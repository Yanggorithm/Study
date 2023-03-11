import sys
from collections import deque
input = sys.stdin.readline

def is_valid(nr, nc):
    return 0 <= nr < N and 0 <= nc < M

def is_clean(r, c):
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if is_valid(nr, nc) and rooms[nr][nc] == 1:
            return False
    return True

N, M = map(int, input().split())
rr, rc, vd = map(int, input().split())
rooms = [list(map(int, input().split())) for _ in range(N)]
rr -= 1
rc -= 1
clean_room = 0

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 보는 방향 : 반시계 방향, 후진 방향
view = {
    0: (3, 2),
    1: (0, 3),
    2: (1, 0),
    3: (2, 1)
}

q = deque()
q.append((rr, rc, vd))
while q:

    r, c, d = q.popleft()
    print(r, c, d)
    # 현재 위치가 더러운 경우 청소한다.
    if rooms[r][c] == 1:
        rooms[r][c] = 0
        clean_room += 1
    # 주변이 더러운지 확인한다.
    if is_clean(r, c):
        # 깨끗하다면 후진
        nd = view[d][1]
        nr = r + dr[nd]
        nc = c + dc[nd]
        # 후진이 가능하다면 후진
        if is_valid(nr, nc):
            # 후진했기 때문에 보는 방향은 그대로
            q.append((nr, nc, d))
        # 후진이 불가능하다면 작동 정지
        else:
            break
    # 주변이 더럽다면 반시계 방향으로 돌기
    else:
        # 반 시계 방향 보기
        nd = view[d][0]
        # 바라보는 방향을 기준으로 앞 쪽
        nr = r + dr[nd]
        nc = c + dc[nd]
        if is_valid(nr, nc):
            if rooms[nr][nc] == 1:
                # 한 칸 전진한다.
                q.append((nr, nc, nd))
            # 깨끗한 경우
            else:
                q.append((r, c, nd))

print(clean_room)
for line in rooms:
    print(line)
