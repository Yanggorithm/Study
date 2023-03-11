import sys
from collections import deque
input = sys.stdin.readline
def can_go(nr, nc, r, c):
    return abs(nr - r) + abs(nc - c) <= 1000

T = int(input())
for tc in range(1, T+1):
    # 편의 점의 개수
    N = int(input())
    convenience_store = deque()
    sang_r, sang_c = map(int, input().split())
    for _ in range(N):
        r, c = map(int, input().split())
        convenience_store.append((r, c))
    rock_r, rock_c = map(int, input().split())
    q = deque()
    q.append((sang_r, sang_c))
    visited = [0] * (N+1)
    ans = "sad"
    while q:
        r, c = q.popleft()
        if can_go(r, c, rock_r, rock_c):
            ans = "happy"
            break
        for idx in range(N):
            if not visited[idx]:
                cr, cc = convenience_store[idx]
                if can_go(cr, cc, r, c):
                    visited[idx] = 1
                    q.append((cr, cc))
    print(ans)