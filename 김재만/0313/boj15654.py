# N과 M (5)

def perm(arr):

    if len(perm_arr) == m:
        print(" ".join(map(str,perm_arr)))
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            perm_arr.append(arr[i])
            perm(arr)
            visited[i] = 0
            perm_arr.pop()


n, m = map(int, input().split())

n_list = list(map(int,input().split()))
visited = [0] * n
n_list.sort()

result = []
perm_arr = []

perm(n_list)