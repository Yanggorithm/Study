# N과 M (6)

def comb(arr):

    if len(perm_arr) == m:
        print(" ".join(map(str,perm_arr)))
        return

    start = arr.index(perm_arr[-1]) if perm_arr else 0
    for i in range(start,n):
        if not visited[i]:
            visited[i] = 1
            perm_arr.append(arr[i])
            comb(arr)
            visited[i] = 0
            perm_arr.pop()


n, m = map(int, input().split())

n_list = list(map(int,input().split()))
visited = [0] * n
n_list.sort()

result = []
perm_arr = []

comb(n_list)