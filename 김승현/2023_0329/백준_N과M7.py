N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
lst = []
def check(cnt):
    if cnt == M:
        print(*lst)
        return

    for i in range(N):
        lst.append(num_list[i])
        check(cnt + 1)
        lst.pop()

check(0)