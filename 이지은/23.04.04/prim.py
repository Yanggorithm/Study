'''
6 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51 
'''


# s : 시작 정점
# V : 정점의 개수
def prim(s, V):
    MST = [0] * (V + 1)  # MST 포함 여부
    MST[s] = 1
    # 최소 신장트리 가중치 합
    maxv = 0
    # 우리가 V개의 정점을 연결할 것
    for _ in range(V):
        u = 0  # 어떤 i랑 연결된 j 중에 최소 가중치를 가진 정점(연결할 정점)
        minV = 10000  # 연결된 정점중 최소 가중치를 찾을 것

        # MST에 포함된 정점 i와 인접한 정점 j 중에서 MST에 포함되지 않고
        # 가중치가 최소인 정점 u를 찾기
        for i in range(V + 1):
            if MST[i] == 1:
                for j in range(V + 1):
                    # i와 j가 연결되어 있고
                    # j는 지금까지 내가 만든 트리에 포함 x
                    # 새로 연결할 j는 최소 가중치를 가져야 한다
                    if adjm[i][j] > 0 and MST[j] == 0 and minV > adjm[i][j]:
                        # 새로 연결할 u 는 j 가 된다.
                        u = j
                        minV = adjm[i][j]
        maxv += minV
        MST[u] = 1

    return maxv


V, E = map(int, input().split())
adjm = [[0] * (V + 1) for _ in range(V + 1)]

for _ in range(E):
    s, e, w = map(int, input().split())
    # 가중치가 있는 무방향 그래프
    adjm[s][e] = w
    adjm[e][s] = w

print(prim(0, V))
