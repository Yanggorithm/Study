import sys
from heapq import heappop, heappush
input = sys.stdin.readline
max_heap = []
N = int(input())
for _ in range(N):
    x = int(input())
    if x:
        heappush(max_heap, -x)
    else:
        if max_heap:
            print(-heappop(max_heap))
        else:
            print(0)