from collections import deque

t = int(input())

def solve(q):
    while q:
        ci = q.popleft()
        if ci == m:
            return visited[ci]

        for ni in (ci+1, ci-1, ci*2, ci-10):
            if 0 <= ni < len(visited) and not visited[ni]:
                visited[ni] = visited[ci] + 1
                q.append(ni)
    

for tc in range(1, t+1):
    n, m = map(int, input().split())
    visited = [0] * (m+11)
    q = deque([n])
    visited[n] = 1
    ans = solve(q)
    print(f"#{tc} {ans-1}")