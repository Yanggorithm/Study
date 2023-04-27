t = int(input())

INF = 10000


# s : 시작 정점
def dijkstra(s, V):
    U = [0] * (V + 1)
    U[s] = 1  
    D[s] = 0  

    for e, w in adjl[s]:
        D[e] = w

    # 남은 정점의 비용을 결정
    for _ in range(n):
        minV = INF
        t = 0
        
        for i in range(n + 1):
            if U[i] == 0 and minV > D[i]:
                minV = D[i]
                t = i
      
        U[t] = 1
       
        for e, w in adjl[t]:
            D[e] = min(D[e], D[t] + w)

for tc in range(1, t+1):
    n, e = map(int, input().split())
    adjl = [[] for _ in range(n + 1)]
    for _ in range(e):
        s, e, w = map(int, input().split())
        adjl[s].append([e, w])

   
    D = [INF] * (n + 1)
   
    dijkstra(0, n)
    print(f"#{tc} {D[n]}")
        