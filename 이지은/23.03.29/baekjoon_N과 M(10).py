import sys

n, m = map(int, sys.stdin.readline().split())
arr = sorted(list(map(int, sys.stdin.readline().split())))
selected = [0] * n

def solve(i):
    if sum(selected) == m:
        tmp = ""
        for i in range(n):
            if selected[i]:
                tmp += str(arr[i])
                tmp += " "
        result.add(tmp)
        return
    
    if i == n:
        return
    
    for j in range(i, n):
        selected[j] = 1
        solve(i+1)
        selected[j] = 0

result = set()
solve(0)
ans = []
for i in result:
    t = list(map(int, i.split()))
    ans.append(t)

for a in sorted(ans):
    print(' '.join(list(map(str, a))))