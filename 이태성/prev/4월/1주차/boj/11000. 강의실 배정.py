import sys, heapq
input = sys.stdin.readline
N = int(input())
q = sorted([list(map(int, input().split())) for _ in range(N)])
room = []
print(q)
heapq.heappush(room, q[0][1])
for i in range(1, N):
    print(i, room)
    if q[i][0] < room[0]:
        heapq.heappush(room, q[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, q[i][1])
print(room)