import sys
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


chicken = []
house = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            chicken.append((i, j))
        elif arr[i][j] == 1:
            house.append((i, j))

def select(i, tmp):
    global result
    if len(tmp) == m:
        result.append(tmp.copy())
        return
    
    if len(tmp):
        result.append(tmp.copy())
    
    for j in range(i, len(chicken)):
        tmp.append(chicken[j])
        select(j+1, tmp)
        tmp.pop()
        
result = []
q = deque([])


def chicken_dist(r):
    c_dist = [0] * len(house)
    for ci, cj in r:
        for h in range(len(house)):
            if c_dist[h] == 0:
                c_dist[h] = abs(house[h][0]-ci)+abs(house[h][1]-cj)
            elif c_dist[h] > abs(house[h][0]-ci)+abs(house[h][1]-cj):
                c_dist[h] = abs(house[h][0]-ci)+abs(house[h][1]-cj)
    return sum(c_dist)

select(0, [])
min_dist = 2*n**3


for r in result:
    tmp_dist = chicken_dist(r)
    if 0 < tmp_dist < min_dist:
        min_dist = tmp_dist

print(min_dist)
    




