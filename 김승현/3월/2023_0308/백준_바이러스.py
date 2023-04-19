
def bfs(G, v, n):
    global result
    visited = [0] * (n + 1)
    q = []
    q.append(v)
    visited[v] = 1

    while q:
        t = q.pop(0)
        for i in G[t]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1
                result.append(i)


N = int(input())
E = int(input())
result = []

num_list = [[] for _ in range(N + 1)]
for i in range(E):
    start, end = map(int, input().split())

    num_list[start].append(end)
    num_list[end].append(start)

bfs(num_list, 1, N)
print(len(result))
