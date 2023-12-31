import sys
import copy
input = sys.stdin.readline

def is_valid(nr, nc):
    return 0 <= nr < N and 0 <= nc < M

# 감시 구역을 체크해주는 함수
def watch(copy_office, node, sr, sc):
    for d in node:
        nr = sr
        nc = sc
        while True:
            nr += dr[d]
            nc += dc[d]
            if not is_valid(nr, nc):
                break
            if copy_office[nr][nc] == 6:
                break
            elif copy_office[nr][nc] == 0:
                copy_office[nr][nc] = 9

def dfs(depth, office):
    global minV

    # [1] 종료조건
    # 깊이가 cctv의 개수와 같다면 함수 종료
    if depth == len(cctv_locations):
        cnt = 0
        # 사각지대를 찾는 반복문
        for r in range(N):
            for c in range(M):
               if office[r][c] == 0:
                   cnt += 1

        if minV > cnt:
            minV = cnt
        return

    # 복사된 사무실
    copy_office = copy.deepcopy(office)
    cctv_num, r, c = cctv_locations[depth]
    for node in cctv[cctv_num]:
        watch(copy_office, node, r, c)
        dfs(depth+1, copy_office)
        # 현재의 사무실을 다시 복사해둔다.
        copy_office = copy.deepcopy(office)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# cctv가 감시할 수 있는 방향을 나타낸 node
cctv = [
    [],
    [[0], [1], [2], [3]],
    [[2, 3], [0, 1]],
    [[0, 3], [3, 1], [1, 2], [2, 0]],
    [[0, 2, 3], [0, 3, 1], [3, 1, 2], [1, 2, 0]],
    [[0, 1, 2, 3]]
]

N, M = map(int, input().split())
cctv_locations, office = [], []
for r in range(N):
    office.append(list(map(int, input().split())))
    for c in range(M):
        if 0 < office[r][c] < 6:
            number = office[r][c]
            cctv_locations.append((number, r, c))

minV = 65
dfs(0, office)
print(minV)
