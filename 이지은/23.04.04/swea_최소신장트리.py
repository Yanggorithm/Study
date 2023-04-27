t = int(input())


def find_set(x):
    while x != rep[x]:
        x = rep[x]

    return x


def union(x, y):
    rep[find_set(y)] = find_set(x)


for tc in range(1, t+1):
    v, e = map(int, input().split())

    arr = []
    for _ in range(e):
        n1, n2, w = map(int, input().split())
        arr.append((w, n1, n2))

    arr.sort()
    rep = [i for i in range(v+1)]

    cnt = 0
    total = 0
    n = v+1
    for w, n1, n2 in arr:
        if find_set(n1) != find_set(n2):
            cnt += 1
            union(n1, n2)
            total += w
            if cnt == n-1:
                break
    
    print(f"#{tc} {total}")
