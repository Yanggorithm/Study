import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

def solve(i, tmp):
    if len(tmp) == m:
        result.append(tmp.copy())
        return
    
    if i == n:
        return
    
    for j in range(i, n):
        tmp.append(arr[j])
        solve(i, tmp)
        tmp.pop()
    
result = []
solve(0, [])

for r in sorted(result):
    print(' '.join(list(map(str, r))))