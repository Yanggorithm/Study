from collections import deque
Soo, YoungS = map(int, input().split())
V = [-1 for _ in range(100001)]
V[Soo] = 0
q = deque()
q.append(Soo)
while q:
    now = q.popleft()
    if now == YoungS:
        break
    for next in (now-1, now+1, now*2):
        if next > 0:
            if V[next] == -1:
                if next == now*2:
                    V[next] = V[now]
                else:
                    V[next] = V[now] + 1
            else:
                if next == now*2:
                    V[next] = min(V[next], V[now])
                else:
                    V[next] = min(V[next], V[now]+1)
        q.append(next)
print(V[YoungS])
