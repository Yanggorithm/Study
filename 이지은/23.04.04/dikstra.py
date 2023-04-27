'''
5 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5
'''

INF = 10000


# s : 시작 정점
def dijkstra(s, V):
    U = [0] * (V + 1)
    U[s] = 1  # 최소 비용이 결정된 정점 표시
    D[s] = 0  # 출발점 비용을 결정

    # 시작지점 s와 연결된 곳을 살펴보고 최소 비용 최신화
    # s와 연결된 e번 정점, 가중치 w에 대해서
    for e, w in adjl[s]:
        D[e] = w

    # 남은 정점의 비용을 결정
    for _ in range(V):
        # 비용이 아직 결정되지 않은 t 정점을 찾자
        # 그중에 D[t] 최소인 t를 찾고 싶다
        minV = INF
        t = 0
        # 최소인 t를 찾으러 가자
        for i in range(V + 1):
            if U[i] == 0 and minV > D[i]:
                minV = D[i]
                t = i
        # 최소인 t를 찾았다
        U[t] = 1
        # 이전까지 내가 알고있던 비용과 새로 경로가 만들어 졌을때 비용 
        # 그 중에서 최소값을 선택해서 최신화
        for e, w in adjl[t]:
            D[e] = min(D[e], D[t] + w)


V, E = map(int, input().split())
adjl = [[] for _ in range(V + 1)]
for _ in range(E):
    s, e, w = map(int, input().split())
    adjl[s].append([e, w])

# D[i] 는 시작정점 a 에서 i까지 가는데 걸리는 최소 비용
D = [INF] * (V + 1)
# 시작정점을 0번이라고 했을때 다른정점으로 가는 최소 비용 계산
dijkstra(0, V)
print(D)
