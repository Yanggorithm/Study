def getdist(x1, y1, x2, y2):
    return abs(x1-x2)+abs(y1-y2)


def dfs(i, x, y, way):
    global minV
    if i == n:
        way += getdist(x, y, hi, hj)
        if way < minV:
            minV = way
        return

    for j in range(n):
        if visited[j] == 0:
            visited[j] = 1
            dfs(i+1, customer[j][0], customer[j][1], way + getdist(x, y, customer[j][0], customer[j][1]))
            visited[j] = 0


t = int(input())

for tc in range(1, t+1):
    n = int(input())
    wi, wj, hi, hj, *arr = map(int, input().split())

    customer = []
    for i in range(0, n*2, 2):
        customer.append(tuple(arr[i: i+2]))

    minV = 100000
    visited = [0] * n
    dfs(0, wi, wj, 0)

    print(f"#{tc} {minV}")
