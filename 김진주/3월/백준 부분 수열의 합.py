def dfs(n, sm, cnt):
    global ans

    if n == N:
		if sm == S and cnt > 0:
			ans += 1
			return


	dfs(n + 1, sm + lst[n], cnt + 1)
	dfs(n + 1, sm, cnt)


N, S = map(int, input().split())
lst = list(map(int, input().split()))
ans = 0
dfs(0, 0, 0)
print(ans)

'''
n, s = map(int, input().split())
num_lst = list(map(int, input().split()))
cnt = 0

def dfs(num, sum):
    global cnt
    if num >= n:
        return
    sum += num_lst[num]
    if sum == s:
        cnt += 1
    dfs(num + 1, sum)
    dfs(num + 1, sum - num_lst[num])
dfs(0, 0)
print(cnt)
'''

'''
5 0
-7 -3 -2 5 8


1
'''