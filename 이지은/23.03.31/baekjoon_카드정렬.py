import sys
import heapq

n = int(sys.stdin.readline().strip())

lst = []
for _ in range(n):
    heapq.heappush(lst, int(sys.stdin.readline().strip()))

ans = 0
while len(lst) > 1:
    a = heapq.heappop(lst)
    b = heapq.heappop(lst)
    ans += (a+b)
    heapq.heappush(lst, a+b)

print(ans)