import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
stack = []
visited = [0] * N

def back(depth, start):
    if depth == M:
        print(" ".join(map(str, stack)))
        return
    prev = 0
    for idx in range(start, N):
        if visited[idx] == 0 and prev != numbers[idx]:
            visited[idx] = 1
            stack.append(numbers[idx])
            prev = numbers[idx]
            back(depth+1, idx+1)
            visited[idx] = 0
            stack.pop()
back(0, 0)
