N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
lst = []
def check(cnt):
    if len(lst) == M:
        print(*lst)
        return

    for i in range(cnt, N):
        lst.append(num_list[i])
        check(i)
        lst.pop()

check(0)