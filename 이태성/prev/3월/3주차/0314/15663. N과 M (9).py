import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
stack = []
visited = [0] * N
prev = 0
# visited 배열을 설정해야 한다.
def backtracking(depth):
    prev = 0
    if depth == M:
        print(" ".join(map(str, stack)))
        return
    for idx in range(N):
        if numbers[idx] != prev and visited[idx] == 0:
            prev = numbers[idx]
            stack. append(numbers[idx])
            visited[idx] = 1
            backtracking(depth+1)
            stack.pop()
            visited[idx] = 0

backtracking(0)

