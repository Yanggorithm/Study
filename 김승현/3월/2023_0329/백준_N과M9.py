N, M = map(int, input().split())
num_list = list(map(int, input().split()))
visited = [0] * N
result = set()
def check(cnt, lst):
    global result

    if cnt == M:
        lst = tuple(lst)
        result.add(lst)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            lst.append(num_list[i])
            check(cnt + 1, lst)
            visited[i] = 0
            lst.pop()

check(0, [])
result = list(result)
result.sort()
for i in result:
    print(*i)