import sys

n, s = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))

def solve(i, val_list):
    global ans
    if val_list and sum(val_list) == s:
        ans += 1

    if i == n:
        return

    for j in range(i, n):
        val_list.append(arr[j])
        solve(j+1, val_list)
        val_list.pop()

ans = 0
selected = [0] * n
solve(0, [])
print(ans)
