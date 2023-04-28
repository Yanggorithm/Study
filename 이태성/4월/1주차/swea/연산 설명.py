from collections import deque

def bfs():
    q = deque()
    # 현재 값을 q에 넣어준다.
    q.append(N)
    # 방문배열에 1을 넣지 않고 시작

    while q:
        nowV = q.popleft()
        # 현재 값이 M일 경우에 V의 값을 리턴해준다.
        if nowV == M:
            return V[M]

        # 새로운 값을 만들어주고
        for newV in (nowV-1, nowV+1, nowV*2, nowV-10):
            # 새로운 값이 해당 범위에 들어가는지 확인하고
            # 방문배열에 없으면 넣어준다.
            # 방문배열에 없다는 말은 이미 도달하지 못했다는 말이므로
            # 최소연산 횟수를 구할 때 먼저 온 쪽이 최소 연산이 된다.
            if 0 <= newV <= M+10 and not V[newV]:
                # 연산을 이제 시작해준 것이기 때문에
                # 처음부터 V에 1을 넣지 않고 시작한다.
                V[newV] = V[nowV] + 1
                # 새로운 값을 넣어준다.
                q.append(newV)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 방문배열을 M+11로 한 이유는
    # 어차피 100을 만들 때 111로 만들 필요는 없기 때문이다.
    # 즉 뺄 값이 10밖에 안되는데 굳이 10 이상을 더해줘서 뺄 필요는 없다는 말이다.
    V = [0] * (M+11)
    print(f"#{tc} {bfs()}")
