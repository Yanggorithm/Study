N, M = map(int, input().split())
num_list = list(map(int, input().split()))
result = set()

def check(cnt, lst):
    global result

    if cnt == M:
        lst = tuple(lst)
        result.add(lst)
        return

    for i in range(N):
        lst.append(num_list[i])
        check(cnt + 1, lst)
        lst.pop()

check(0, [])
result = list(result)
result.sort()
for i in result:
    print(*i)