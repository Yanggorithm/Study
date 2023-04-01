'''
길이 M인 수열 모두 구하기
중복 수열 X
'''
def dfs(n, lst):
    if n == M:
        ans.append(lst)
        return

    prev = 0
    for i in range(N):
        if v[i] == 0 and prev != A[i]:
            v[i] = 1
            prev = A[i]
            dfs(n+1, lst+[A[i]])
            v[i] = 0

N, M = map(int, input().split())
A = sorted(map(int, input().split()))
ans = []
v = [0] * N
dfs(0, [])
for lst in ans:
    print(*lst)