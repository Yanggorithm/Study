import sys
from collections import deque

def is_valid(nr, nc):
    return 0 <= nr < N and 0 <= nc < M

input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N, M = map(int, input().split())
campus = []
do_r, do_c = 0, 0
not_found_doyeon = True
for r in range(N):
    line = list(input().strip())
    if not_found_doyeon:
        for c in range(M):
            if line[c] == "I":
                do_r = r
                do_c = c
                not_found_doyeon = False
    campus.append(line)
met_people_cnt = 0
q = deque()
q.append((do_r, do_c))
campus[do_r][do_c] = "X"
while q:
    r, c = q.popleft()
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if is_valid(nr, nc) and campus[nr][nc] != "X":
            if campus[nr][nc] == "P":
                met_people_cnt += 1
            campus[nr][nc] = "X"
            q.append((nr, nc))
if met_people_cnt:
    print(met_people_cnt)
else:
    print("TT")
