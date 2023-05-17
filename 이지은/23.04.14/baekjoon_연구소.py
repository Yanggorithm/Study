"""
풀이 접근 방법
1. 벽을 세울 3곳을 정한다.
    벽을 세울 곳 정하는 방법?
        - 빈칸인지 아닌지 판단해서 벽 후보지에 추가
        - 벽 후보지 중에 itertools combination으로 세군데 선정

2. 벽을 세운 뒤 바이러스가 퍼지는지 안퍼지는지 확인한다. ==> 시간초과 안날까..?
    - 빈칸의 개수가 0이 되면 바이러스 퍼짐
    - 빈칸의 개수가 1 이상이면 안퍼짐, 최대값 갱신
"""
from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
arr, blank, virus = [], [], deque([])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 0 : 빈칸, 1 : 벽, 2: 바이러스
for i in range(n):
    t = input().strip().split()
    arr.append(t)
    for j in range(m):
        if t[j] == '0':
            blank.append((i, j))
        elif t[j] == '2':
            virus.append((i, j))

q = deque([])

result = 0
for wall in combinations(blank, 3):
    num = len(blank)-3
    visited = [[0] * m for _ in range(n)]

    # 벽을 세운다.
    for wi, wj in wall:
        arr[wi][wj] = '1'
    
    q.extend(virus)
    
    # 바이러스 확산
    while q:
        ci, cj = q.popleft()
        for d in range(4):
            ni, nj = ci + dx[d], cj + dy[d]
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == '0' and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                q.append((ni, nj))
                num -= 1                
    
    if num:
        if num > result:
            result = num
    
    # 다음 조합 순서를 위해 벽을 다시 복구해준다.
    for wi, wj in wall:
        arr[wi][wj] = '0'

print(result)



