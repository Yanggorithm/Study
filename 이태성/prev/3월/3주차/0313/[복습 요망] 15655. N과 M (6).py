import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
stack = []
def backtracking(start):
    if len(stack) == M:
        print(" ".join(map(str, stack)))
        return
    for i in range(start, N):
        if lst[i] not in stack:
            stack.append(lst[i])
            backtracking(i+1)
            stack.pop()
backtracking(0)