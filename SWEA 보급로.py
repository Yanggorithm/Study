'''
중복 허용 !!
범위 내 이동할 위치 더 적은 비용
이동할 위치의 비용 >   현 위치 비용 + 현위치 -> 다음 위치 비용
   visit[ni][nj] > visit[ci][cj] + arr[ni][nj]
'''
INF = 10000
def bfs(si, sj, ei, ej):
    q = []
    q.append((si, sj))
    visit = [[INF] * n for _ in range(n)]
    print(visit)
    visit[si][sj] = arr[si][sj]

    while q:
        ci, cj = q.pop(0)

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < n and visit[ni][nj] > visit[ci][cj] + arr[ni][nj]:
                q.append((ni, nj))
                visit[ni][nj] = visit[ci][cj] + arr[ni][nj]

    print(visit)
    return visit[ei][ej]


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]

    si = sj = 0
    ei = ej = n-1
    ans = bfs(si, sj, ei, ej)

    print(f'#{tc} {ans}')