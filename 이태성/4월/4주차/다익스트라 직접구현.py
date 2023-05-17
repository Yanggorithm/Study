import sys
input = sys.stdin.readline

# 입력 받기
n = int(input())
m = int(input())
adjL = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    adjL[a].append((b, c))
start, end = map(int, input().split())

# 초기화
visited = [False] * (n + 1)
distance = [sys.maxsize] * (n + 1)
distance[start] = 0

# 다익스트라 알고리즘
for _ in range(n):
    # 최단 거리가 가장 짧은 노드 찾기
    now = 0
    min_distance = sys.maxsize
    for i in range(1, n + 1):
        if not visited[i] and distance[i] < min_distance:
            now = i
            min_distance = distance[i]
    visited[now] = True

    # 현재 노드와 연결된 노드들의 최단 거리 갱신
    for node, dist in adjL[now]:
        cost = distance[now] + dist
        if cost < distance[node]:
            distance[node] = cost

# 출력
print(distance[end])
