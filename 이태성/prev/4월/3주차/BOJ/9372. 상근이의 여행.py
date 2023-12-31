import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def kruskal(edges, n):
    parent = [i for i in range(n+1)]
    edges.sort(key=lambda x: x[2])
    result = 0
    for edge in edges:
        a, b, cost = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost
    return result

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        a, b = map(int, input().split())
        edges.append((a, b, 1))
    print(kruskal(edges, N))
