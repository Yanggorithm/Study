from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n = int(input().strip())
k = int(input().strip())
# 보드 생성
arr = [[0]*(n+1) for _ in range(n+1)]

# 사과 위치 표시
for _ in range(k):
    r, c = map(int, input().strip().split())
    arr[r][c] = 2

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
    q = [(1, 1)]
    arr[1][1] = 1
    # ti, tj : 꼬리 위치
    ti, tj = 1, 1
    # 시간
    time = 1
    # 방향
    d = 0
    # 꼬리
    tail = deque([(1, 1)])

    while q:
        ci, cj = q.pop()
        
        # 이동
        ni, nj = ci+dx[d], cj+dy[d]
        # 보드 내에 위치
        if 0 < ni <= n and 0 < nj <= n:
            # 몸
            if arr[ni][nj] == 1:
                return time
            # 빈공간이면 꼬리 이동
            elif arr[ni][nj] == 0:
                ti, tj = tail.popleft()
                arr[ti][tj] = 0
            
            # 예비 꼬리 위치
            tail.append((ni, nj))            
            # 머리 이동
            arr[ni][nj] = 1
            # 머리 위치 추가
            q.append((ni, nj))

        # 벽에 부딪혔다면
        elif ni == 0 or ni == n+1 or nj == 0 or nj == n+1:
            # 시간반환
            return time
        
        # 남은 방향 전환이 있을 경우
        if direction:
            # 방향 전환할 시간?
            if time == direction[0][0]:
                x, c = direction.popleft()
                # 오른쪽 90도
                if c == 'D':
                    d = (d+1)%4
                # 왼쪽 90도
                else:
                    d -= 1
                    if d == -1:
                        d = 3
        
        time += 1
        
        
print(solve())