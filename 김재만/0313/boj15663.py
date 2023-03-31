# N과 M (9)

def perm(arr):

    if len(perm_arr) == m:
        ans = perm_arr[:]
        result[tuple(ans)] = 1
        return


    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            perm_arr.append(arr[i])
            perm(arr)
            perm_arr.pop()
            visited[i] = 0


n, m = map(int, input().split())

n_list = list(map(int,input().split()))
visited = [0] * n
n_list.sort()

result = dict()
perm_arr = []

perm(n_list)

for i in result.keys():
    print(" ".join(map(str,i)))