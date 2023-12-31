import sys
from heapq import heappop, heappush
import heapq
input = sys.stdin.readline
n, m = map(int, input().split())
cards = list(map(int, input().split()))
heap = []
for card in cards:
    heappush(heap, card)
while m:
    num1 = heappop(heap)
    num2 = heappop(heap)
    sum_numbers = num1 + num2
    heappush(heap, sum_numbers)
    heappush(heap, sum_numbers)
    m -= 1
print(sum(heap))