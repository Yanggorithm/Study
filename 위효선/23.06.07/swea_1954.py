#SWEA_1954_달팽이숫자

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def is_valid(r,c):
    return 0 <= r < N and 0 <= c < N

T = int(input())
for TC in range(1,T+1):
    N = int(input())
    nums = list(range(1, N**2+1))

    board = [ [0] * N for _ in range(N)]
    
    tr = tc = d = num = 0
    while num < N**2:
        num += 1
        board[tr][tc] = num

        nr, nc = tr+dr[d%4], tc+dc[d%4]
        if is_valid(nr, nc) and not board[nr][nc]:
            tr, tc = nr, nc
        else:
            d += 1
            tr, tc = tr+dr[d%4], tc+dc[d%4]

    print(f'#{TC}')
         
    for i in range(N):
        print(*board[i])