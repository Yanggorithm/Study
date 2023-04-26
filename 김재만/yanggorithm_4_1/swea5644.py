# 무선 충전

# 풀이중

from collections import deque


def bfs(sx, sy, r, p):

    q = deque()
    q.append((sx, sy))

    # 상하좌우
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    
    cnt = 0
    visited = [[0] * 10 for _ in range(10)]
    bc_map[sx][sy] = p
    visited[sx][sy] = 1

    while q:
        cnt += 1
        for _ in range(len(q)):
            x, y = q.popleft()
            
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
            
                if 0 <= nx < 10 and 0 <= ny < 10 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    bc_map[nx][ny] = p
                    q.append((nx,ny))
            
        if cnt == r:
            break
        


T = int(input())

for tc in range(1, T+1):
    m, a = map(int, input().split())
    route_a = list(map(int, input().split()))
    route_b = list(map(int, input().split()))

    bc_map = [[0] * 10 for _ in range(10)]
    print(bc_map)

    for _ in range(a):
        yy, xx, ran, power = map(int, input().split())
        bfs(xx-1, yy-1, ran, power)

    print(bc_map)