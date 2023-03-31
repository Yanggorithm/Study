# ABCDE
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(start, cnt):
    global flag
    visited[start] = 1
    
    if cnt == 5 :
        flag = 1
        return
    
    for next in adj_list[start]:
        if visited[next] == 0:
            dfs(next, cnt+1)
            
    visited[start] = 0
    return


n, m = map(int,input().split())
adj_list = [[] for _ in range(n)]
visited = [0] * n
flag = 0

for _ in range(m):
    a, b = map(int,input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

for i in range(n):
    if flag == 0:
        visited[i] = 1
        dfs(i, 1)
        visited[i] = 0
    else:
        break

print(flag)