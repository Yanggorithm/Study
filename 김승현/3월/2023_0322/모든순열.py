# N = int(input())

_ = int(input())
N = int(input())

cal = ['+', '-', '*', '/']
cal_list = list(map(int, input().split()))

num_list = list(map(int, input().split()))

cal_res = []
for i in range(4):
    cal_res.extend(cal_list[i] * cal[i])

# num_list = []
# for i in range(1, N + 1):
#     num_list.append(i)

ans = []
visited = [0] * (N - 1)

def dfs(idx):
    if len(ans) == N - 1:
        print(ans)

    for i in range(N - 1):
        if not visited[i]:
            ans.append(cal_res[i])
            visited[i] = 1
            dfs(i)
            visited[i] = 0
            ans.pop()

dfs(0)