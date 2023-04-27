import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

def solve(i):
    if i == n:
        result.add(' '.join(list(map(str, arr[:m]))))
        return
    
    for j in range(i, n):
        arr[i], arr[j] = arr[j], arr[i]
        solve(i+1)
        arr[i], arr[j] = arr[j], arr[i]

result = set()
solve(0)
ans = []

for i in result:
    t = list(map(int, i.split()))
    ans.append(t)

for a in sorted(ans):
    print(' '.join(list(map(str, a))))