import sys
from collections import deque
input = sys.stdin.readline

# 방향 전환을 위한 델타배열
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 보이는 방향을 기준으로 오른쪽으로 갈지 왼쪽으로 갈지 정해주는 배열
# 오른쪽일 경우 r 왼쪽일 경우 l
r_node = [3, 2, 0, 1]
l_node = [2, 3, 1, 0]

# 뱀이 자리를 벗어났는지 확인하는 함수
def is_valid(nr, nc):
    return 0 <= nr < N and 0 <= nc < N

N = int(input())
K = int(input())
# 사과의 위치를 받아주는 함수
apple = []
for _ in range(K):
    r, c = map(int, input().split())
    # r, c 1행 1열이 0행 0열이기 때문에 미리 1을 빼준다.
    apple.append((r-1, c-1))
L = int(input())

# 시간을 지났을 경우에 popleft()를 해주기 위해서 deque을 사용
snake = deque()
for _ in range(L):
    X, C = input().split()
    snake.append((X, C))

# 뱀의 길이를 알 수 있는 함수
# 뱀의 꼬리를 자르기 위해서 deque을 사용
q = deque()
q.append((0, 0))

# 시작부터 오른쪽
nd = 3

# 시간은 0부터
tm = 0

# 시작은 0, 0에서
sr = sc = 0
while True:
    tm += 1
    # 갈 방향을 정해주는 변수 설정
    print(sr, sc)
    nr = sr + dr[nd]
    nc = sc + dc[nd]

    # 이동 배열이 존재 할 경우
    if snake:
        # 우선 X, C는 첫 번째 인덱스의 값을 가져온다.
        X, C = snake[0]
        # 그 시간이 현재 시간일 경우
        if int(X) == tm:
            # 현재 값을 빼주고
            snake.popleft()
            # 오른쪽인지 왼쪽인지 확인 한 뒤
            # 다음 방향을 바꿔준다.
            if C == "D":
                nd = r_node[nd]
            else:
                nd = l_node[nd]

    # 진행 방향이 유효하고 뱀의 몸에 닿지 않는다면
    if is_valid(nr, nc) and (nr, nc) not in q:
        # 현재 위치(뱀의 머리)를 바꿔주고
        sr, sc = nr, nc
        # 지금 가는 곳에 사과가 있다면
        if (nr, nc) in apple:
            # 사과를 지워준다.
            apple.remove((nr, nc))
            # 꼬리는 놔두고 머리만 길어지니까 머리만 추가
            q.append((nr, nc))
        else:
            # 꼬리를 자르고
            q.popleft()
            # 진행 방향 추가
            q.append((nr, nc))

    # 그 외는 범위를 벗어났을 것이고, 몸을 부딪히기 때문에 바로 게임 종료
    else:
        break

print(tm)