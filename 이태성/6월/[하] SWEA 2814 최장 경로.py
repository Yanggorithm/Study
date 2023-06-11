# 깊이 우선 탐색
def dfs(start, V, length):
    global max_length

    # 최장 경로를 최신화 시켜준다.
    if max_length < length:
        max_length = length

    for next in adjL[start]:
        if next not in V:
            dfs(next, V+[next], length+1)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    adjL = [[] for _ in range(N+1)]
    for _ in range(M):
        x, y = map(int, input().split())
        adjL[x].append(y)
        adjL[y].append(x)
    # 최소 길이는 1이기 때문에 max_length는 1
    max_length = 1
    for start in range(1, N+1):
        # 여기서 빈 리스트가 아닌 [start]
        # start를 꼭 넣어주고 시작해야함
        # 0이 아닌 1인 이유는 최소 길이는 1이기 때문에
        dfs(start, [start], 1)
    print(f"#{tc}", max_length)