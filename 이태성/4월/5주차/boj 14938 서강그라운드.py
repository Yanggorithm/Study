import sys, heapq
input = sys.stdin.readline
n, m, r = map(int, input().split())
items = list(map(int, input().split()))
adjL = [[] for _ in range(n+1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    adjL[a].append((b, l))
    adjL[b].append((a, l))

def dijkstra(startingPoint):
    heap = []
    heapq.heappush(heap, (0, startingPoint))
    V = [0 for _ in range(n+1)]
    V[startingPoint] = 1
    itemCnt = items[startingPoint-1]
    while heap:
        currentLength, currentPoint = heapq.heappop(heap)
        for nextPoint, nextLength in adjL[currentPoint]:
            newLength = currentLength + nextLength
            if newLength > m:
                continue
            if V[nextPoint] == 0:
                V[nextPoint] = 1
                itemCnt += items[nextPoint-1]
            heapq.heappush(heap, (newLength, nextPoint))
    return itemCnt

maxCnt = 0
for city in range(1, n+1):
    maxCnt = max(maxCnt, dijkstra(city))
print(maxCnt)