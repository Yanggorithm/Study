N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
result = set()

def check(idx, lst):
    if len(lst) == M:
        lst = tuple(lst)
        result.add(lst)
        return

    for i in range(idx ,N):
        lst.append(num_list[i])
        check(i, lst)
        lst.pop()

check(0, [])
result= list(result)
result.sort()
for i in result:
    print(*i)
