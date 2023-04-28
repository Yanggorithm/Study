import sys
input = sys.stdin.readline
from heapq import heappop, heappush
abs_heap = []
N = int(input())
for _ in range(N):
    x = int(input())
    if x > 0:
        heappush(abs_heap, (x, x))
    elif x < 0:
        heappush(abs_heap, (-x, x))
    else:
        if abs_heap:
            print(heappop(abs_heap)[1])
        else:
            print(0)
