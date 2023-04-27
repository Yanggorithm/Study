import sys

n, m = map(int, sys.stdin.readline().split())
arr = sorted(list(map(int, sys.stdin.readline().split())))

def solve(i, tmp):
    if i == n:
        if len(tmp) == m:
            result.append(tmp.copy())
        return
    
    solve(i+1, tmp+[arr[i]])
    solve(i+1, tmp)

result = []
solve(0, [])

for i in range(len(result)):
    print(' '.join(list(map(str, result[i]))))