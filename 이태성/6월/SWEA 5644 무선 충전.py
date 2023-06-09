from collections import deque
T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 방향 기다림, 위, 오른쪽, 아래, 왼쪽
directions = [(0, 0), (-1, 0), (0, 1), (1, 0), (0, -1)]

# 충전할 수 있는 최대 값을 구해주는 함수
def plus_charge(Ar, Ac, Br, Bc):
    # 글로벌 함수로 total charge를 가져온다.
    global total_charge

    # DP를 이용해서 최대 값을 저장해줌
    new = [0 for _ in range(8)]

    # 사용하기 편하게 A와 B에 다시 저장
    A = test_map[Ar][Ac]
    B = test_map[Br][Bc]

    # 이중 for문을 돌면서 두 개를 더 했을 때 최대 값을 new[i]에 저장
    for i in range(8):
        for j in range(8):
            # i와 j가 같다는 말은 같은 BC를 사용한다는 말인데
            # 굳이 계산 안해줘도 되기 때문에 continue
            # 다시 말해서 같은 BC를 사용한다는 말은 하나의 BC의 충전 값을 2로 나눠야 하기 때문에 그냥 넘어가도 된다
            if i == j:
                continue
            tmp = A[i] + B[j]
            if new[i] < tmp:
                new[i] = tmp
    # new의 최대 값을 저장
    total_charge += max(new)

def is_valid(nr, nc):
    return 0 <= nr < 10 and 0 <= nc < 10

# 범위를 저장해줄 함수
def range_BC(sr, sc, D, order, charge):
    q = deque()
    q.append((sr, sc, 0))
    test_map[sr][sc][order] = charge
    while q:
        r, c, length = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if is_valid(nr, nc) and length < D and not test_map[nr][nc][order]:
                test_map[nr][nc][order] = charge
                q.append((nr, nc, length+1))

for tc in range(1, T+1):
    N, cnt_BC = map(int, input().split())
    # 처음 값도 쉽게 계산하기 위해 0을 맨 앞에 저장
    A = [0] + list(map(int, input().split()))
    B = [0] + list(map(int, input().split()))

    # 충전량을 보여주는 그래프를 만든다.
    # 3차원 배열
    # 8개의 공간에 0을 넣어서 BC의 충전량을 순서대로 저장하려한다.
    test_map = [[[0 for _ in range(8)] for _ in range(10)] for _ in range(10)]
    for order in range(cnt_BC):
        c, r, D, charge = map(int, input().split())
        range_BC(r-1, c-1, D, order, charge)

    total_charge = 0
    Ar, Ac = 0, 0
    Br, Bc = 9, 9
    for idx in range(N+1):
        # 다음 A의 위치 B의 위치를 업데이트
        Ar += directions[A[idx]][0]
        Ac += directions[A[idx]][1]
        Br += directions[B[idx]][0]
        Bc += directions[B[idx]][1]

        # 업데이트한 위치를 바탕으로 무선충전시작
        plus_charge(Ar, Ac, Br, Bc)
    print(f"#{tc}", total_charge)