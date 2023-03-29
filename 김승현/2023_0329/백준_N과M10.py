N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
result = set()
def check(idx, lst):
    global result

    if len(lst) == M:
        lst = tuple(lst)
        result.add(lst)
        return

    for i in range(idx, N):
        check(i + 1, lst + [num_list[i]])

check(0, [])
result = list(result)
result.sort()
for i in result:
    print(*i)