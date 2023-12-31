dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def is_valid(nr, nc):
    return 0 <= nr < N and 0 <= nc < N

def dfs(sr, sc, check, length):
    global maxL
    for d in range(4):
        nr = sr + dr[d]
        nc = sc + dc[d]

        # [1] 범위와 방문을 확인하자.
        # 우선 방문 하지 않았어야 하고,
        # 범위가 유효해야 하는 것은 기본이다.

        if is_valid(nr, nc) and V[nr][nc] == 0:
            # [2] 기본 조건을 먼저 충족시켜준다.
            # 깎고 안깎고는 나중일이기 때문에 깎기 전에 갈 수 있는지 확인하고 돌아준다.
            # 현재 높이보다 낮은 곳으로 간다고 했다.
            if mountain[nr][nc] < mountain[sr][sc]:
                V[nr][nc] = 1
                dfs(nr, nc, check, length+1)
                V[nr][nc] = 0

            # [3] 특이 조건을 확인하자.
            # 현재 높이보다 높은 경우에 한 번 깎아도 된다고 했다.
            # 그렇기 때문에 높은지 먼저 확인하고, 깎았는지를 확인해준다.
            elif check == 0 and mountain[nr][nc] >= mountain[sr][sc]:
                # 얼마나 깎을지를 정해준다.
                # 깊이가 내가 파고 싶은 만큼이기 때문에 반복문을 통해 구현해야 한다.
                # 쉽게 말해서 K가 3인경우 1만큼 파고 백트래킹 2만큼 파고 백트래킹 3만큼 파고 백트래킹을 해준다.
                for k in range(1, K+1):
                    # 산 k만큼 파버리기~
                    mountain[nr][nc] -= k
                    if mountain[nr][nc] < mountain[sr][sc]:
                        V[nr][nc] = 1
                        # 여기서 이미 1회 팠기 때문에 cnt가 1이 된다.
                        dfs(nr, nc, 1, length+1)
                        V[nr][nc] = 0
                    # 산 다시 매꿔버리기~
                    mountain[nr][nc] += k
    maxL = max(maxL, length)
    return

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    mountain = []
    maxH = 0
    for r in range(N):
        mountain.append(list(map(int, input().split())))
        for c in range(N):
            # 가장 높은 곳을 기점으로 가야하므로 높이를 찾아준다.
            maxH = max(maxH, mountain[r][c])

    maxL = 0
    V = [[0 for _ in range(N)] for _ in range(N)]
    for sr in range(N):
        for sc in range(N):
            # 가장 높은 봉우리가 아니면 지나가요~
            if mountain[sr][sc] != maxH:
                continue
            # 방문해주고
            V[sr][sc] = 1
            # 가장 높은 곳에서 시작인데,
            # length는 당연히 1부터 시작
            # 지금 봉우리를 포함한 거리이기 때문이다.
            dfs(sr, sc, 0, 1)
            V[sr][sc] = 0

    print(f"#{tc} {maxL}")