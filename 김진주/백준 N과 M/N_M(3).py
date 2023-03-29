'''
3. 같은 수 여러번 가능
중복 수열 X
'''
def dfs(n, lst):
    if n == M:
        ans.append(lst)
        return

    for i in range(1, N+1):
        dfs(n+1, lst+[i])

N, M = map(int, input().split())
ans = []
dfs(0, [])

for lst in ans:
    print(*lst)
'''
4 2
1 1
1 2
1 3
1 4
2 1
2 2
2 3
2 4
3 1
3 2
3 3
3 4
4 1
4 2
4 3
4 4
'''