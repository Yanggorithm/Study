def solution(rows, columns, queries):
    newMap = [[0 for _ in range(columns)] for _ in range(rows)]
    
    cnt = 1
    for r in range(rows):
        for c in range(columns):
            newMap[r][c] = cnt
            cnt += 1
    answer = []
    for x1, y1, x2, y2 in queries:
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        minV = 10001
        nextV = newMap[x1][y1]
        # 상단
        for ny in range(y1+1, y2+1):
            if minV > nextV:
                minV = nextV
            newMap[x1][ny], nextV = nextV, newMap[x1][ny]

        # 오른쪽
        for nx in range(x1+1, x2+1):
            if minV > nextV:
                minV = nextV
            newMap[nx][y2], nextV = nextV, newMap[nx][y2]

        # 하단
        for ny in range(y2-1, y1-1, -1):
            if minV > nextV:
                minV = nextV
            newMap[x2][ny], nextV = nextV, newMap[x2][ny]

        # 왼쪽
        for nx in range(x2-1, x1-1, -1):
            if minV > nextV:
                minV = nextV
            newMap[nx][y1], nextV = nextV, newMap[nx][y1]
        answer.append(minV)

        
    return answer