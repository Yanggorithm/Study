# 백준 1715
# 스터디 문제
# 카드 정렬하기
# 힙으로 ?
import sys
import heapq

input = sys.stdin.readline

n = int(input())
n_list = []
for _ in range(n):
    n_list.append(int(input()))
heapq.heapify(n_list)

ans = 0
while len(n_list) > 1:
    tmp = 0
    for _ in range(2):
        tmp += heapq.heappop(n_list)
    heapq.heappush(n_list, tmp)
    ans += tmp

print(ans)
