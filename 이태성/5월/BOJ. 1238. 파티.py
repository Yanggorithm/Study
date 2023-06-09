import sys
import heapq
input = sys.stdin.readline
# N명의 학생, M개의 단 방향 도로, X마을
N, M, X = map(int, input().split())
# 인접 배열
adjL = [[] for _ in range(N+1)]
# 무한값
INF = int(1e9)

for _ in range(M):
    # 시작지점, 도착지점, 소요시간
    startingPoint, endpoint, timeRequired = map(int, input().split())
    adjL[startingPoint].append((endpoint, timeRequired))

# 다익스트라 함수 구현
def dijkstra(startingPoint):
    heap = []

    timeVisited = [INF for _ in range(N+1)]
    heapq.heappush(heap, (0, startingPoint))
    # 현재 지점 초기화
    timeVisited[startingPoint] = 0
    while heap:
        # 현재 소요시간, 현재 지점
        currentTimeRequired, nowPoint = heapq.heappop(heap)

        # 현재 소요시간이 지금 방문 시간 보다 크면
        # 최소 시간이 아니기 때문에 continue
        if timeVisited[nowPoint] < currentTimeRequired :
            continue

        # 다음 방문할 지점, 다음 방문할 지점의 소요시간
        for nextPoint, nextTimeRequired in adjL[nowPoint]:
            # currentTimeRequired += nextTimeRequired
            # 위의 값은 틀린 값
            # 새로운 소요시간 = 현재 소요시간 + 다음 소요 시간
            newtimeRequired = currentTimeRequired + nextTimeRequired

            # 소요 시간을 비교해서 방문 시간에 넣어준다.
            if timeVisited[nextPoint] > newtimeRequired:
                timeVisited[nextPoint] = newtimeRequired
                heapq.heappush(heap, (newtimeRequired, nextPoint))

    # 방분시간 배열을 반환
    return timeVisited

ans = 0
# X에서 각 마을까지 도달한 최단시간
back = dijkstra(X)
for i in range(1, N+1):
    # X까지 가는데 걸리는 최단시간
    go = dijkstra(i)
    # 최단 시간 + 최단시간이 가장 큰 시간을 ans에 저장
    ans = max(ans, go[X]+back[i])
print(ans)