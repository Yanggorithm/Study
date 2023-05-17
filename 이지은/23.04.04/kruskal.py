rep = []


def find_set(x):
    while x != rep[x]:
        x = rep[x]

    return x


def union(x, y):
    rep[find_set(y)] = find_set(x)


V, E = map(int, input().split())
edge = []
for _ in range(E):
    s, e, w = map(int, input().split())
    edge.append([w, s, e])

edge.sort()
rep = [i for i in range(V + 1)]

# 내가 지금까지 선택한 간선의 개수
cnt = 0
# MST 가중치의 합
total = 0
# MST 의 간선수 N  = 정점수 - 1
N = V + 1
for w, s, e in edge:
    # s 집합의 대표와 e 집합의 대표가 달라야 사이클이 x
    if find_set(s) != find_set(e):
        cnt += 1
        union(s, e)
        total += w
        # MST 구성이 끝나면 종료
        if cnt == N - 1:
            break

print(total)
