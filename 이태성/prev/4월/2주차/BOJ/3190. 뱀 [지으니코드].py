from collections import deque
from pprint import pprint
import sys

input = sys.stdin.readline

def change_direction(ti, tj, td):
    for d in range(4):
        ni = ti + dx[d]
        nj = tj + dy[d]
        if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 1:
            return d
    return td


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n = int(input().strip())
k = int(input().strip())
# 보드 생성
arr = [[0] * n for _ in range(n)]

# 사과 위치 표시
for _ in range(k):
    r, c = map(int, input().strip().split())
    arr[r-1][c-1] = 2

l = int(input().strip())
direction = deque([])
for _ in range(l):
    x, c = input().strip().split()
    x = int(x)
    direction.append((x, c))


# 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.
# 1 : 뱀의 몸, 2 : 사과

def solve():
    # 초기위치
    q = [(0, 0)]
    arr[0][0] = 1
    # ti, tj : 꼬리 위치
    ti, tj, td = 0, 0, 3
    # 시간
    time = 0
    # 방향
    d = 0
    while q:
        # print(f"===={time}====")
        # pprint(arr)

        ci, cj = q.pop()

        # 남은 방향 전환이 있을 경우
        if direction:
            # 방향 전환할 시간?
            x, c = direction.popleft()
            if time == x:
                # 오른쪽 90도
                if c == 'D':
                    d = (d + 1) % 4
                # 왼쪽 90도
                else:
                    d -= 1
                    if d == -1:
                        d = 3
        # 이동
        ni, nj = ci + dx[d], cj + dy[d]
        # 보드 내에 위치
        if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] != 1:

            # 빈공간이면 꼬리 이동
            if arr[ni][nj] == 0:
                arr[ti][tj] = 0
                arr[ni][nj] = 1
                td = change_direction(ti, tj, td)
                ti, tj = ti + dx[td], tj + dy[td]

            arr[ni][nj] = 1
            # 머리 위치 추가
            q.append((ni, nj))
        # 벽에 부딪혔다면
        else:
            # 시간반환
            return time

        time += 1

print(solve()+1)
