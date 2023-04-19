from collections import deque
import sys

N, K = map(int, sys.stdin.readline().strip().split())


visited = [0] * 100001

def bfs(n):
    q = deque()
    q.append(n)
    while q:
        num  = q.popleft()
        
        if num == K:
            break
        else:
            for i in (num - 1, num + 1, num * 2):
                if 0 <= i <= 100000 and not visited[i]:
                    visited[i] = visited[num] + 1    
                    q.append(i)           
    
    return visited[num]
        
print(bfs(N))
        