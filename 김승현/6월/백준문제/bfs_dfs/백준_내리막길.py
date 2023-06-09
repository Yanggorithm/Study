import sys
import heapq

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())

map_v = [list(map(int, input().split())) for _ in range(N)]

# 출발 점
s_x, s_y = 0, 0
# 도착 점
e_x, e_y = N - 1, M - 1

# 방문 배열을 통한 DP
visited = [[0] * M for _ in range(N)]


def check(sx, sy):
    q = []
    # max heap을 사용한 문제
    heapq.heappush(q, (-map_v[sx][sy], sx, sy))
    visited[sx][sy] = 1

    while q:
        value, x, y = heapq.heappop(q)

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            # heapq를 통해 크기가 큰 것 부터 확인해야함
            # 그냥 bfs를 사용하니 간선 길이가 다 1이라고 판단하기 때문
            if 0 <= nx < N and 0 <= ny < M and map_v[x][y] > map_v[nx][ny]:
                if not visited[nx][ny]:
                    heapq.heappush(q, (-map_v[nx][ny], nx, ny))

                visited[nx][ny] += visited[x][y]


check(s_x, s_y)
print(visited[e_x][e_y])