'''
1. 중복 X
'''

def dfs(n, lst):
    if n == M:
        ans.append(lst)
        return

    for i in range(1, N+1):
        if v[i] == 0:
            v[i] = 1
            dfs(n+1, lst+[i])
            v[i] = 0

N, M = map(int, input().split())
ans = []
v = [0] * (N+1)
dfs(0, [])

for lst in ans:
    print(*lst)
'''
4 2
1 2
1 3
1 4
2 1
2 3
2 4
3 1
3 2
3 4
4 1
4 2
4 3
'''