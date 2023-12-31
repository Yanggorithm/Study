import sys
import heapq
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

# 무한을 의미하는 값으로 10억을 설정
# 최단 경로를 찾기 위해서 적당히 큰 수를 저장
INF = int(1e9)

# 파라미터로 현재 위치와 adjL(인접행렬) 거리 배열을 가져옴
def dijkstra(start):
    heap = []
    # 힙에 현재 거리와, 현재 위치를 저장
    heapq.heappush(heap, (0, start))
    # 현재 거리를 0으로 초기화
    costVisited[start] = 0
    # heap이 들어있을 경우
    while heap:
        # 현재 까지 드는 비용, 현재 위치를 빼준다.
        currentCost, now = heapq.heappop(heap)

        # 가지치기
        # 현재 금액이 이전에 있던 금액보다 많으면 갈 필요가 없다.
        if costVisited[now] < currentCost:
            continue

        # 다음 갈 곳의 드는 비용 cost
        # 현재 위치에서 갈 수 있는 다음 위치 next
        for cost, next in adjL[now]:
            # 현재까지 든 비용에 다음 갈 곳의 드는 비용을 더해준다.
            currentCost += cost
            if currentCost < costVisited[next]:
                costVisited[next] = currentCost
                heapq.heappush(heap, (currentCost, next))

# 입력 받기
n = int(input())
m = int(input())
adjL = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    adjL[a].append((b, c))
start, end = map(int, input().split())

# 최소 비용 계산
costVisited = [INF] * (n + 1)
dijkstra(start)

# 출력
print(costVisited[end])
