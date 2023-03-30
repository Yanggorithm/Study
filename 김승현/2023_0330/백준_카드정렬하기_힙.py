import heapq
import sys

input = sys.stdin.readline

N = int(input())
num_heap = []

for i in range(N):
    heapq.heappush(num_heap, int(input()))

result = 0

while num_heap:
    if len(num_heap) == 1:
        break
    else:
        ans = heapq.heappop(num_heap) + heapq.heappop(num_heap)
        result += ans
        heapq.heappush(num_heap, ans)

print(result)