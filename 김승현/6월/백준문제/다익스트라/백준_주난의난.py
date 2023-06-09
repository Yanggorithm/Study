import sys
from collections import deque
from pprint import pprint


input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
sx, sy, ex, ey = map(int, input().split())

map_v = [list(input().strip()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

res_list = deque()
q = deque()
q.append((sx - 1, sy - 1))
res_list.append((sx - 1, sy - 1))
visited[sx - 1][sy - 1] = 1


def bfs1():

    while q:
        x, y = q.popleft()
        # print(x, y)
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and map_v[nx][ny] == '0':
                visited[nx][ny] = 1
                q.append((nx, ny))
                res_list.append((nx, ny))

bfs1()

def bfs2():
    cnt = 0

    while res_list:
        cnt += 1

        for _ in range(len(res_list)):
            x, y = res_list.popleft()

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if 0 <= nx < N and 0 <= ny < M:
                    if nx == ex - 1 and ny == ey - 1:
                        return cnt

                    if map_v[nx][ny] == '0':
                        q.append((nx, ny))
                    elif map_v[nx][ny] == '1':
                        map_v[nx][ny] = '0'
                        res_list.append((nx, ny))
                        q.append((nx, ny))

        # pprint(map_v)
        # print(q)
        bfs1()

t = bfs2()
print(t)