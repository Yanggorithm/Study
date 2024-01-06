# 프로그래머스 공원 산책

directions = {
    'E' : (0, 1),
    'W' : (0, -1),
    'S' : (1, 0),
    'N' : (-1, 0)
             }

def isValid(r, c, n, m) :
    return 0 <= r < n and 0 <= c < m

def solution(park, routes):
    n = len(park)
    m = len(park[0])
    
    for i in range(n):
        for j in range(m):
            if park[i][j] == 'S':
                sr, sc = i, j
                break
                
    for move in routes:
        direction = move[0]
        num = int(move[-1])
        tr, tc = sr, sc
        
        for d in range(1, num+1):
            nr = tr + directions[direction][0] * d
            nc = tc + directions[direction][1] * d        
            if not isValid(nr, nc, n, m) or park[nr][nc] == 'X':
                break
        else:
            sr, sc = nr, nc
                                
    return [sr,sc]