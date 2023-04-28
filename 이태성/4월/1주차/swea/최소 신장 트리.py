def get_p(x):
    if parent[x] != x:
        parent[x] = get_p(parent[x])
        return parent[x]

def union_p(x, y):
    p = get_p(x)
    q = get_p(y)
    if p > q:
        parent[p] = q
    else:
        parent[q] = p

def find(x, y):
    return get_p(x) == get_p(y)

T = int(input())
for tc in range(1, T+1):
    ans = 0
    V, E = map(int, input().split())
    parent = [num for num in range(V+1)]
    edge = sorted([list(map(int, input().split())) for _ in range(E)], key=lambda x: -x[2])

    while edge:
        n1, n2, w = edge.pop()
        if not find(n1, n2):
            union_p(n1, n2)
            ans += w

    print(f"#{tc} {ans}")