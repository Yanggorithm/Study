import sys

n, m = map(int, sys.stdin.readline().split())
arr = sorted(set(list(map(int, sys.stdin.readline().split()))))

def solve(i, tmp):
    if len(tmp) == m:
        print(' '.join(list(map(str, tmp))))
        return
    
    if i == n:
        return
    
    for j in range(i, len(arr)):
        tmp.append(arr[j])
        solve(j, tmp)
        tmp.pop()

solve(0, [])