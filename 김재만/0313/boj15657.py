# N과 M (8)

def perm(arr):

    if len(perm_arr) == m:
        print(" ".join(map(str,perm_arr)))
        return
    
    start = n_list.index(perm_arr[-1]) if perm_arr else 0
    for i in range(start,n):
        perm_arr.append(arr[i])
        perm(arr)
        perm_arr.pop()


n, m = map(int, input().split())

n_list = list(map(int,input().split()))
n_list.sort()

result = []
perm_arr = []

perm(n_list)