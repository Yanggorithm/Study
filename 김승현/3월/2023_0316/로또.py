N = 6


def dfs(idx, cnt):
    if cnt == N:
        print(*result)
        return

    for i in range(idx, k):
        result.append(num_list[i])
        dfs(i + 1, cnt + 1)
        result.pop()


while True:
    arr = list(map(int, input().split()))
    k = arr[0]
    num_list = arr[1:]
    result = []
    dfs(0, 0)
    if k == 0:
        exit()
    print()

