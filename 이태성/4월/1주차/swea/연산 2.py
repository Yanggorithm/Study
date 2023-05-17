from collections import deque
def bfs(N, cnt):
    q = deque()
    q.append((N, cnt))
    V = set()
    V.add(N)

    while q:
        N, cnt = q.popleft()

        if N == M:
            return cnt

        if N * 2 not in V and 1 <= N * 2 <= 1000000:
            q.append((N*2, cnt+1))
            V.add(N*2)
        if N + 1 not in V and 1 <= N + 1 <= 1000000:
            q.append((N+1, cnt+1))
            V.add(N+1)
        if N - 1 not in V and 1 <= N - 1 <= 1000000:
            q.append((N-1, cnt+1))
            V.add(N-1)
        if N - 10 not in V and 1 <= N - 10 <= 1000000:
            q.append((N-10, cnt+1))
            V.add(N-10)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    print(f"#{tc} {bfs(N, 0)}")
