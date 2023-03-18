import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
N, M = map(int, input().split())
adjL = [[] for _ in range(N)]
for _ in range(M):
    start, to = map(int, input().split())
    adjL[start].append(to)
    adjL[to].append(start)
visited = [0] * N
ans = 0
def back(S, depth):
    visited[S] = 1
    global ans
    if depth == 4:
        ans = 1
        return
    for num in adjL[S]:
        if visited[num] == 0:
            visited[num] = 1
            back(num, depth+1)
            visited[num] = 0

for num in range(N):
    back(num, 0)
    visited[num] = 0
    if ans:
        break
print(ans)