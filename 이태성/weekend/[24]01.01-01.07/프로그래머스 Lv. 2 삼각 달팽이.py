def solution(n):
    top = [[0 for _ in range(n)] for _ in range(n)]
    number = 1
    cnt = n
    ifd = [0, 1, 2]
    direction = 0
    startIndex = 0
    endIndex = n
    # index 증가, 고정, 감소, 증가, 고정, 감소
    while cnt:
        cnt -= 1
        d = ifd[direction]
        if d == 0:
            for idx in range(startIndex, endIndex):
                top[idx][startIndex] = number
                number += 1
            startIndex += 1
        elif d == 1:
            for jdx in range(startIndex, endIndex):
                top[endIndex - 1][jdx] = number
                number += 1
            endIndex -= 1
        else:
            for idx in range(endIndex - 1, startIndex - 1, -1):
                top[idx][endIndex] = number
                number += 1
            startIndex += 1
        direction = (direction + 1) % 3
    answer = []
    for idx in range(n):
        for jdx in range(n):
            number = top[idx][jdx]
            if number:
                answer.append(number)
    return answer
