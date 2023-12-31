import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(depth):
    global max_cal
    if depth == N:
        max_cal = max(max_cal, cal(stack))
        return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            stack.append(A[i])
            dfs(depth+1)
            stack.pop()
            visited[i] = 0

def cal(stack):
    tot = 0
    for i in range(N-1):
        tot += abs(stack[i] - stack[i+1])
    return tot

N = int(input())
A = list(map(int, input().split()))
stack = []
visited = [0] * N
max_cal = 0
dfs(0)
print(max_cal)
