# N과 M (11)

def comb(arr):

    if len(comb_list) == m:
        result[tuple(comb_list)] = 1
        return

    for i in range(n):
        comb_list.append(n_list[i])
        comb(arr)
        comb_list.pop()


n, m = map(int,input().split())

n_list = list(map(int,input().split()))
visited = [0] * n
n_list.sort()

comb_list = []
result = dict()

comb(n_list)
for k in result.keys():
    print(" ".join(map(str,k)))