import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())
adjL = [[] for _ in range(N+1)]
maxVisited = set()
for num in range(1, N+1):
    nowNumber = int(input())
    if num == nowNumber:
        maxVisited.add(num)
    adjL[num].append(nowNumber)
# 한바퀴 돌고 다시 원점으로 돌아오면 된다.
def dfs(start, S, visited, cnt):
    global maxCnt, maxVisited
    if cnt > 0:
        if start == S:
            maxVisited = maxVisited.union(visited)

    for next in adjL[S]:
        if next in visited:
            return
        dfs(start, next, visited+[next], cnt+1)

for num in range(1, N+1):
    dfs(num, num, [], 0)

print(len(maxVisited))
for num in sorted(list(maxVisited)):
    print(num)