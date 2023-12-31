import sys
from collections import deque
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def backtracking(cnt):
    if cnt == M:
        print(' '.join(map(str, q)))
        return
    for num in lst:
        if visited[num] == 0:
            visited[num] = 1
            q.append(num)
            backtracking(cnt + 1)
            q.pop()
            visited[num] = 0

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
q = deque()
visited = [0] * 10001
backtracking(0)