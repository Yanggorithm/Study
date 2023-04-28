import sys
from heapq import heappop, heappush
input = sys.stdin.readline
N = int(input())
board = []
for _ in range(N):
    line = list(map(int, input().split()))
    for num in line:
        # 개수를 유지하면서 저장하면 되는 구조
        if len(board) < N:
            heappush(board, num)
        else:
            if board[0] < num:
                heappop(board)
                heappush(board, num)

print(board[0])
