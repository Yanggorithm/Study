# N과 M (7)

def perm(arr):

    if len(perm_arr) == m:
        print(" ".join(map(str,perm_arr)))
        return

    for i in range(n):
        perm_arr.append(arr[i])
        perm(arr)
        perm_arr.pop()


n, m = map(int, input().split())

n_list = list(map(int,input().split()))
n_list.sort()

result = []
perm_arr = []

perm(n_list)