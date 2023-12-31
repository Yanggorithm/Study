import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
stack = []
def backtracking(depth):
    if depth == M:
        print(" ".join(map(str, stack)))
        return
    for idx in range(N):
        stack.append(numbers[idx])
        backtracking(depth+1)
        stack.pop()
backtracking(0)