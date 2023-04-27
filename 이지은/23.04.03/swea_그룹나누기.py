t = int(input())

def union(x, y):
    nx = find_set(x)
    ny = find_set(y)
    t[find_set(y)] = find_set(x)
    for k in range(1, n+1):
        if t[k] == ny:
            t[k] = nx

def find_set(x):
    if x == t[x]:
        return x
    else:
        return find_set(t[x])


for tc in range(1, t+1):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    
    t = [i for i in range(n+1)]
    
    for i in range(0, 2*m, 2):
        a, b = lst[i], lst[i+1]
        union(a, b)
        
    cnt = 0
    for i in range(1, n+1):
        if t.count(i) == 0:
            continue
        elif t.count(i) == 1:
            cnt += 1
        else:
            cnt += 1
    
    print(f"#{tc} {cnt}")