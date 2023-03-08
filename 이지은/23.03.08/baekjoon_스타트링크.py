import sys
from collections import deque

f, s, g, u, d = map(int, sys.stdin.readline().strip().split())
def solve():
    if (s < g and u == 0) or (s > g and d == 0):
        return "use the stairs"
    elif s==g:
        return 0    
    else:
        q = deque([s])
        floor = [-1] * (f+1)
        floor[s] = 0

        while q:
            c = q.popleft()
            if c == g:
                break

            for i in (+u, -d):
                n = c + i
                if 0 < n <= f and floor[n] == -1:
                        floor[n] = floor[c] + 1
                        q.append(n)
        if floor[g] == -1:
            return "use the stairs"
        else:
            return floor[g]

print(solve())