def dfs(S):
    global length
    for num in adjL[S]:
        if not V[num]:
            V[num] = 1
            dfs(num)
            # 어차피 왔던 곳으로 돌아갈 필요 없으니 0으로 초기화 하지 않는다.

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    adjL = [[] for _ in range(N+1)]
    arr = list(map(int, input().split()))
    for i in range(M):
        adjL[arr[i*2]].append(arr[i*2+1])
        adjL[arr[i*2+1]].append(arr[i*2])

    V = [0] * (N + 1)
    cnt = 0
    # 1번 부터 시작해서 가보는데
    # 어차피 돈 곳은 V[num]이 1일 것이기 때문에
    # continue를 통해서 지나간다.
    for num in range(1, N+1):
        if V[num]:
            continue
        V[num] = 1
        dfs(num)
        # 방문하지 않았다는 말은 그룹이 아니라는 말이므로 cnt + 1
        cnt += 1

    print(f"#{tc}", cnt)