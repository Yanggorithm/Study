import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
# 중복 없는 순열 만들기
def dfs(S, D):
    if D == 6:
        print(" ".join(map(str, stack)))
        return
    for i in range(S, K+1):
        stack.append(numbers[i])
        dfs(i+1, D+1)
        stack.pop()

while True:
    numbers = list(map(int, input().split()))
    if numbers[0] == 0:
        break
    K = numbers[0]
    stack = []
    dfs(1, 0)
    print()
