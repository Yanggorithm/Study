from collections import deque
def solution(n, computers):
    answer = 0
    adjL = [[] for _ in range(n+1)]
    for i in range(n):
        for j in range(i, n):
            if i == j:
                continue
            if computers[i][j]:
                adjL[i+1].append(j+1)
                adjL[j+1].append(i+1)
                
    V = [0 for _ in range(n+1)]
    for start in range(1, n+1):
        if V[start]:
            continue
        V[start] = 1
        answer += 1
        q = deque()
        q.append(start)
        while q:
            current = q.popleft()
            for next in adjL[current]:
                if V[next]:
                    continue
                V[next] = 1
                q.append(next)   
    return answer