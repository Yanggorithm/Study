import sys
from collections import deque

n = int(sys.stdin.readline())
p1, p2 = map(int, sys.stdin.readline().strip().split())
m = int(sys.stdin.readline())
arr = [[] for _ in range(101)]
for _ in range(m):
    x, y = map(int, sys.stdin.readline().strip().split())
    arr[x].append(y)
    arr[y].append(x)

q = deque([p1])
v = [0] * 101

def solve():
    while q:
        ni = q.popleft()
        if ni == p2:
            return v[p2]
        
        for a in arr[ni]:
            if v[a] == 0:
                v[a] = v[ni] + 1
                q.append(a)
    
    return -1

print(solve())
        
        
            





