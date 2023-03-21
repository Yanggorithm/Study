N = int(input())
V = [0] * (N+1)
stack = []
def dfs(depth):
    if depth == N:
        print(" ".join(map(str, stack)))
    for num in range(1, N+1):
        if V[num] == 0:
            V[num] = 1
            stack.append(num)
            dfs(depth+1)
            stack.pop()
            V[num] = 0
dfs(0)