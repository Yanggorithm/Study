import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))

def solve(i):
    global maxV
    tmp = 0
    if i == n:
        for j in range(0, n, 2):
            tmp += abs(arr[j] - arr[j+1])
        if tmp > maxV:
            maxV = tmp
    
    for j in range(i, n):
        arr[i], arr[j] = arr[j], arr[i]
        solve(i+1)
        arr[i], arr[j] = arr[j], arr[i]

maxV = 0
solve(0)
print(maxV)