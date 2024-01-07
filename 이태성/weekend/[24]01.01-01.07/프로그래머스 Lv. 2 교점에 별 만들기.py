def solution(line):
    lenLine = len(line)
    
    def isValid(A, B, C, D):
        return A * D - B * C
    
    def uniqueFC(A, B, C, D, E, F, divide):
        x = (B * F - E * D) / divide
        y = (E * C - A * F) / divide
        return x, y
    
    stars = set()
    for i in range(lenLine-1):
        A, B, E = line[i]
        for j in range(i+1, lenLine):
            if i == j:
                continue
            C, D, F = line[j]
            divide = A * D - B * C
            if divide:
                x, y = uniqueFC(A, B, C, D, E, F, divide)
                if float(x).is_integer() and float(y).is_integer():
                    stars.add((x, y))
   
    stars = list(stars)
    xStars = sorted(stars)
    minX, maxX = int(xStars[0][0]), int(xStars[-1][0])
    stars = sorted(stars, key=lambda x: -x[1])
    maxY, minY = int(stars[0][1]), int(stars[-1][1])
    answer = [["." for _ in range(maxX-minX+1)] for _ in range(maxY-minY+1)]
    for x, y in stars:
        nx = abs(int(x) - minX)
        ny = abs(int(y) - maxY)
        answer[ny][nx] = "*"
    result = []
    
    for ans in answer:
        str = ""
        for a in ans:
            str += a
        result.append(str)
    return result