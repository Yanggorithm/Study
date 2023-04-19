N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
visited = [0] * N
def check(cnt, lst):
    if cnt == M:
        print(*lst)
        return

    for i in range(N):
        if not visited[i]:
            lst.append(num_list[i])
            visited[i] = 1
            check(cnt + 1, lst)
            visited[i] = 0
            lst.pop()

check(0, [])