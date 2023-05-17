import sys

n, m = map(int, sys.stdin.readline().split())
arr = sorted(list(map(int, sys.stdin.readline().split())))

def solve(i, tmp):
    if len(tmp) == m:
        print(' '.join(list(map(str, tmp))))
        return

    if i == n:
        return
    
    for j in range(i, n):
        tmp.append(arr[j])
        solve(j, tmp)
        tmp.pop()

solve(0, [])