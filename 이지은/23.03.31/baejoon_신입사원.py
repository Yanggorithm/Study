import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    arr = []

    for _ in range(n):
        arr.append(tuple(map(int, sys.stdin.readline().strip().split())))

    arr.sort()

    cnt = 0
    minV = arr[0][1]
    for j in range(1, n):
        if arr[j][1] > minV:
            cnt += 1
        minV = min(minV, arr[j][1])
    
    print(n - cnt)