import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input())
min_heap = []
for _ in range(N):
    x = int(input())
    if x:
        heappush(min_heap, x)
    else:
        if min_heap:
            print(heappop(min_heap))
        else:
            print(0)