import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
stack = []
def back(start, depth):
    if depth == M:
        print(" ".join(map(str, stack)))
        return
    prev = 0
    for idx in range(start, N):
        if prev != numbers[idx]:
            stack.append(numbers[idx])
            prev = numbers[idx]
            back(idx, depth+1)
            stack.pop()
back(0, 0)