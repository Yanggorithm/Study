import heapq

# 다익스트라 알고리즘을 구현한 함수
def dijkstra(graph, start):
    # 시작 정점에서의 최단 거리를 저장하는 배열
    distance = [float('inf')] * len(graph)
    distance[start] = 0

    # 우선순위 큐를 사용하여 방문할 정점을 선택
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        dist, current = heapq.heappop(queue)

        # 현재 정점을 이미 처리한 경우, 무시
        if distance[current] < dist:
            continue

        # 현재 정점과 연결된 인접한 정점들을 확인
        for neighbor, weight in graph[current]:
            new_dist = dist + weight

            # 현재까지의 최단 거리보다 더 짧은 경로가 존재하는 경우, 최단 거리를 업데이트하고 큐에 추가
            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                heapq.heappush(queue, (new_dist, neighbor))

    return distance

# 테스트 케이스의 개수 입력
T = int(input())

for test_case in range(1, T + 1):
    # 정점의 개수 N, 간선의 개수 M, 출발 정점의 번호 start, 도착 정점의 번호 end 입력
    N, M, start, end = map(int, input().split())

    # 그래프 초기화
    graph = [[] for _ in range(N + 1)]

    # 간선 정보 입력
    for _ in range(M):
        u, v, weight = map(int, input().split())
        graph[u].append((v, weight))
        graph[v].append((u, weight))

    # 다익스트라 알고리즘으로 최단 경로 계산
    shortest_path = dijkstra(graph, start)

    # 최단 경로 출력
    print(f'#{test_case} {shortest_path[end]}')