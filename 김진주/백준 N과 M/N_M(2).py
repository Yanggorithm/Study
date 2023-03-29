'''
2. 조합 n개중에 r개 뽑기 nCr
순열 P
'''
def dfs(n, lst):
    if n > N:
        if len(lst) == M:
            ans.append(lst)
        return

    dfs(n+1, lst+[n])
    dfs(n+1, lst)


N, M = map(int, input().split())
ans = []
dfs(1, [])

for lst in ans:
    print(*lst)
'''
4 2
1 2
1 3
1 4
2 3
2 4
3 4
'''