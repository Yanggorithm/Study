
N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

def check(cnt, lst):
    if len(lst) == M:
        print(*lst)
        return

    for i in range(cnt, N):
        lst.append(num_list[i])
        check(i + 1, lst)
        lst.pop()

check(0, [])